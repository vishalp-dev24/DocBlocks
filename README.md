# DocBlocks — Layout-Preserving PDF Text Extraction

DocBlocks is a Python library for extracting text from **digitally generated PDFs** while preserving their visual reading order and page structure. It avoids the alignment distortions found in traditional PDF extractors.

> **Note:** DocBlocks works **only with computer-generated (digital) PDFs**.  
> It does **not** support **scanned/image PDFs** at this time.

---

## Purpose

Most extraction libraries produce output that is:

- misaligned
- reordered
- merged across columns
- missing sections

DocBlocks solves this by providing:

- accurate reading order
- non-destructive extraction
- page-based segmentation
- zero content modification

**Final mission:** _no more ugly alignment at the end._

---

## Guarantees

DocBlocks guarantees:

- no text modification
- no text deletion
- no page merging
- no reordering beyond true reading order
- **one page’s content will never interfere with another page**

This ensures perfect segmentation for AI/ML pipelines, RAG systems, or document processing.

---

## Current Limitations

DocBlocks **does not support**:

- scanned/image PDFs
- OCR-based text extraction
- non-PDF formats (Word, images, HTML)

This limitation is intentional to guarantee perfect handling of **digital text PDFs**.

---

## Roadmap (Planned for End of February Release)

The upcoming version will include:

- support for additional document formats
- OCR engine for scanned documents
- richer layout information
- improved block detection

OCR engine names are intentionally not mentioned — expect **powerful, production-grade** OCR.


---


## Installation

```bash
pip install docblocks
```

Requires Python **3.8+**

---

## Usage

### Extract text into memory

```python
import docblocks

text = docblocks.extract(r"document.pdf")
print(text)
```

### Convert PDF → TXT file

```python
import docblocks

docblocks.convert(
    r"document.pdf",
    r"output.txt"
)
```

You must use `r"..."` (raw strings) for Windows paths to avoid escape issues.

---

## Output Format

DocBlocks ensures:

- clean page segmentation
- pure reading order
- no cross-page interference
- no ugly alignment errors

Example output:

```
┌──────── PAGE 1 ─────────┐
This is page one content...
└──────────────────────────┘

┌──────── PAGE 2 ─────────┐
This is page two content...
└──────────────────────────┘
```

Notice that:

> **Page 1 content never flows into Page 2, and Page 2 never leaks into Page 1.**

---

## Best For

DocBlocks is ideal for:

- research papers
- legal & policy docs
- technical manuals
- structured reports
- AI preprocessing (RAG / LLM input)

---

## License

MIT — free for commercial & academic use.

---

## Vision

DocBlocks exists for one purpose:

> “No more ugly alignment at the end.”

---

## Contributing

Issues and suggestions are welcome:

https://github.com/vishalp-dev24/DocBlocks.git

Pull requests, feedback, and feature requests are appreciated.
