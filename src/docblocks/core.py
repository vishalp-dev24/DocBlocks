from docblocks.io.pdf_reader import load_pdf
from docblocks.export.text_exporter import to_exact_text

def extract(input_path: str) -> str:
    pages = load_pdf(input_path)

    # Exact extraction: no block parsing, no removals
    page_texts = [page.get_text("text", flags=0) for page in pages]

    return to_exact_text(page_texts)

def convert(input_path: str, output_path: str):
    text = extract(input_path)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
