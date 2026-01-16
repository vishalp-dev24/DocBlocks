# DocBlocks

**PDF to structured text with page segmentation.**

DocBlocks is a simple, lightweight Python utility for extracting text from PDF files and preserving page breaks in a clean, readable format. It wraps the powerful `PyMuPDF` library to provide a straightforward command-line interface for PDF-to-text conversion.

The key feature is its "exact text" export, which adds clear page separators to the output, making it easy to see where each page begins and ends.

## How It Works

The script reads a PDF file page by page. For each page, it extracts the raw text content and then wraps it in a formatted block with a header and footer.

**Example Output:**

```
┌──────── PAGE 1 ─────────┐
This is the text content from the first page of the PDF.
All text is preserved exactly as it appears.
└──────────────────────────┘

┌──────── PAGE 2 ─────────┐
This is the content from the second page.
...
└──────────────────────────┘
```

## Installation

This project uses Python and requires the `PyMuPDF` library.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vishalp-dev24/docblocks.git
    cd docblocks
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install -e .
    ```

## Usage

DocBlocks provides a simple command-line interface.

```bash
docblocks <input_pdf_path> <output_text_path>
```

### Arguments

-   `input_pdf_path`: The full path to the source PDF file.
-   `output_text_path`: The full path where the extracted text will be saved.

### Example

```bash
docblocks r"C:\Users\YourUser\Documents\report.pdf" r"C:\Users\YourUser\Documents\report.txt"
```

This will create a new file `report.txt` with the content extracted from `report.pdf`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
