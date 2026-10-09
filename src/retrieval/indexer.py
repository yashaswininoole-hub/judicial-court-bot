"""Builds and saves the FAISS index + chunk metadata from the PDFs in data/raw."""

import json
from pathlib import Path

import faiss

from src.retrieval.chunker import chunk_pages
from src.retrieval.document_loader import extract_pdf
from src.retrieval.vector_store import build_index

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "data" / "raw"
INDEX_DIR = ROOT / "data" / "index"
INDEX_PATH = INDEX_DIR / "legal.index"
CHUNKS_PATH = INDEX_DIR / "chunks.json"


def build_and_save_index(verbose: bool = True) -> int:
    """Read every PDF in data/raw, chunk, embed, and write the index files.

    Returns the number of chunks indexed.
    Raises FileNotFoundError if there are no PDFs, ValueError if no text is found.
    """
    pdfs = sorted(RAW_DIR.glob("*.pdf"))
    if not pdfs:
        raise FileNotFoundError(f"No PDFs found in {RAW_DIR}. Add PDFs and try again.")

    chunks: list[dict] = []
    for path in pdfs:
        pages = extract_pdf(path)
        page_chunks = chunk_pages(pages)
        if verbose:
            print(f"{path.name}: {len(pages)} text pages, {len(page_chunks)} chunks")
        chunks.extend(page_chunks)

    if not chunks:
        raise ValueError("No extractable text found. Scanned PDFs need OCR first.")

    index = build_index(chunks)

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(INDEX_PATH))
    with CHUNKS_PATH.open("w", encoding="utf-8") as file:
        json.dump(chunks, file, ensure_ascii=False, indent=2)

    if verbose:
        print(f"Built index with {len(chunks)} chunks at {INDEX_DIR}")
    return len(chunks)