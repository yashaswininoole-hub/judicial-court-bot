"""Run from repository root: python scripts/build_index.py"""
import json
from pathlib import Path
import faiss

from src.retrieval.document_loader import extract_pdf
from src.retrieval.chunker import chunk_pages
from src.retrieval.vector_store import build_index

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
INDEX_DIR = ROOT / "data" / "index"


def main():
    pdfs = sorted(RAW_DIR.glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDFs found in {RAW_DIR}. Add official PDFs and run again.")
    chunks = []
    for path in pdfs:
        pages = extract_pdf(path)
        page_chunks = chunk_pages(pages)
        print(f"{path.name}: {len(pages)} text pages, {len(page_chunks)} chunks")
        chunks.extend(page_chunks)
    if not chunks:
        raise SystemExit("No extractable text found. Scanned PDFs need OCR first.")
    index = build_index(chunks)
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(INDEX_DIR / "legal.index"))
    with (INDEX_DIR / "chunks.json").open("w", encoding="utf-8") as file:
        json.dump(chunks, file, ensure_ascii=False, indent=2)
    print(f"Built index with {len(chunks)} chunks at {INDEX_DIR}")


if __name__ == "__main__":
    main()
