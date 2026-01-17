import pytest
import os
import fitz
import docblocks
from docblocks.io.pdf_reader import load_pdf

# Helper to create PDF files
@pytest.fixture
def pdf_factory(tmp_path):
    def _create_pdf(name, content="text", encrypted=False, corrupt=False, image_only=False, zero_pages=False):
        p = tmp_path / name
        if corrupt:
            p.write_text("Not a PDF")
            return str(p)

        doc = fitz.open()
        if not zero_pages:
            page = doc.new_page()
            if image_only:
                # Create a minimal image
                img_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
                page.insert_image(page.rect, stream=img_data)
            else:
                page.insert_text((50, 50), content)

        if encrypted:
            doc.save(str(p), encryption=fitz.PDF_ENCRYPT_AES_256, user_pw="user", owner_pw="owner")
        else:
            doc.save(str(p))
        doc.close()
        return str(p)
    return _create_pdf

def test_extract_normal(pdf_factory):
    path = pdf_factory("normal.pdf", content="Hello World")
    text = docblocks.extract(path)
    assert "Hello World" in text
    assert "PAGE 1" in text

def test_extract_encrypted(pdf_factory):
    path = pdf_factory("encrypted.pdf", encrypted=True)
    with pytest.raises(ValueError, match="encrypted"):
        docblocks.extract(path)

def test_extract_corrupt(pdf_factory):
    path = pdf_factory("corrupt.pdf", corrupt=True)
    with pytest.raises(ValueError, match="Failed to open PDF file"):
        docblocks.extract(path)

def test_extract_wrong_type():
    with pytest.raises(TypeError, match="must be a string"):
        docblocks.extract(123)
    with pytest.raises(TypeError, match="must be a string"):
        docblocks.extract(None)

def test_extract_directory(tmp_path):
    d = tmp_path / "folder.pdf"
    d.mkdir()
    # Should raise IsADirectoryError or our custom error
    with pytest.raises((IsADirectoryError, ValueError), match="file"):
        docblocks.extract(str(d))

def test_extract_image_only(pdf_factory):
    path = pdf_factory("image.pdf", image_only=True)
    text = docblocks.extract(path)
    # Should be empty of content text, but contain page markers
    assert "PAGE 1" in text
    # The text content between markers should be empty or just newlines
    lines = text.splitlines()
    # PAGE 1 header, empty line, footer, empty line
    # Depending on formatting.
    # Just check that no text is found (we didn't add any).
    assert "Hello" not in text

def test_extract_missing_file():
    with pytest.raises(FileNotFoundError):
        docblocks.extract("non_existent.pdf")

def test_extract_wrong_extension(tmp_path):
    p = tmp_path / "test.txt"
    p.write_text("content")
    with pytest.raises(ValueError, match="must be a .pdf file"):
        docblocks.extract(str(p))
