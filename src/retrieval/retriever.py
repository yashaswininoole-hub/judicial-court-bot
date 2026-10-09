import json
import traceback

import faiss

from src.retrieval.indexer import CHUNKS_PATH, INDEX_PATH, build_and_save_index
from src.retrieval.vector_store import search_index

_index = None
_chunks = None


def _ensure_index_files() -> bool:
    """Build the index automatically on first use if it doesn't exist yet."""
    if INDEX_PATH.exists() and CHUNKS_PATH.exists():
        return True
    print("JurisAI: index not found, building it from data/raw (first run only)...")
    try:
        build_and_save_index(verbose=True)
    except Exception:
        traceback.print_exc()
        return False
    return INDEX_PATH.exists() and CHUNKS_PATH.exists()


def _load():
    """Load the index and chunks once and keep them in memory."""
    global _index, _chunks
    if _index is None or _chunks is None:
        if not _ensure_index_files():
            return None, None
        _index = faiss.read_index(str(INDEX_PATH))
        with CHUNKS_PATH.open(encoding="utf-8") as file:
            _chunks = json.load(file)
    return _index, _chunks


def retrieve_context(question: str, top_k: int = 5) -> list[dict]:
    """Return passages as {text, source, page}; [] if nothing can be retrieved."""
    if not question or not question.strip():
        return []
    index, chunks = _load()
    if index is None or not chunks:
        return []
    results = search_index(index, chunks, question, top_k=top_k)
    # Keep the agreed contract stable; scores remain internal to retrieval.
    return [{"text": r["text"], "source": r["source"], "page": r["page"]} for r in results]