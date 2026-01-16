from docblocks.io.pdf_reader import load_pdf

PDF_PATH = "tests/sample.pdf"
OUT_PATH = "sample_output.txt"

pages = load_pdf(PDF_PATH)

output_pages = []

for i, p in enumerate(pages, start=1):
    # extract raw text from page exactly as-is
    raw = p.get_text("text")

    header = f"┌──────── PAGE {i} ─────────┐"
    footer = "└──────────────────────────┘"

    output_pages.append(f"{header}\n{raw}\n{footer}")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write("\n\n".join(output_pages))

print(f"Done! Saved to: {OUT_PATH}")
