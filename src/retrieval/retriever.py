"""Public retrieval interface used by src.pipeline.answer_question."""
import json
from pathlib import Path
import faiss

from src.retrieval.vector_store import search_index

ROOT = Path(__file__).resolve().parents[2]
INDEX_DIR = ROOT / "data" / "index"
INDEX_PATH = INDEX_DIR / "legal.index"
CHUNKS_PATH = INDEX_DIR / "chunks.json"


def retrieve_context(question: str, top_k: int = 5) -> list[dict]:
    """Return passages as {text, source, page}; return [] until index exists."""
    if not question or not question.strip() or not INDEX_PATH.exists() or not CHUNKS_PATH.exists():
        return []
    index = faiss.read_index(str(INDEX_PATH))
    with CHUNKS_PATH.open(encoding="utf-8") as file:
        chunks = json.load(file)
    results = search_index(index, chunks, question, top_k=top_k)
    # Keep the agreed contract stable; scores remain internal to retrieval.
    return [{"text": r["text"], "source": r["source"], "page": r["page"]} for r in results]
