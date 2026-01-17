import fitz
import os

def load_pdf(path: str):
    if not isinstance(path, str):
        raise TypeError(f"Input path must be a string, got {type(path).__name__}")

    if not path.lower().endswith(".pdf"):
        raise ValueError("Input file must be a .pdf file")

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    if not os.path.isfile(path):
        raise ValueError(f"Path is not a file: {path}")

    try:
        doc = fitz.open(path)
    except Exception as e:
        # Wrap fitz errors for corrupt files
        raise ValueError(f"Failed to open PDF file: {e}") from e

    if doc.is_encrypted:
        raise ValueError("PDF is encrypted and cannot be processed without a password")

    return [page for page in doc]
