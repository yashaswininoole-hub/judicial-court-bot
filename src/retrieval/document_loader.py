from pathlib import Path
import fitz


def extract_pdf(pdf_path: str | Path) -> list[dict]:
    """Extract text from a PDF while preserving original 1-based page numbers."""
    path = Path(pdf_path)
    pages = []
    with fitz.open(path) as pdf:
        for page_number, page in enumerate(pdf, start=1):
            text = page.get_text("text").strip()
            if text:
                pages.append({"text": text, "source": path.name, "page": page_number})
    return pages
