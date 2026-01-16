import fitz
import os

def load_pdf(path: str):
    if not path.lower().endswith(".pdf"):
        raise ValueError("Input file must be a .pdf file")

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    doc = fitz.open(path)
    return [page for page in doc]
