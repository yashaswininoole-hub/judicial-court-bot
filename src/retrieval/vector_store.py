import faiss
from src.retrieval.embeddings import embed_texts


def build_index(chunks: list[dict]):
    if not chunks:
        raise ValueError("No chunks found. Add text-based PDFs to data/raw first.")
    vectors = embed_texts([item["text"] for item in chunks])
    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)
    return index


def search_index(index, chunks: list[dict], question: str, top_k: int = 5) -> list[dict]:
    if not chunks or not question.strip():
        return []
    query_vector = embed_texts([question])
    scores, indices = index.search(query_vector, min(top_k, len(chunks)))
    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx < 0:
            continue
        item = chunks[int(idx)]
        results.append({"text": item["text"], "source": item["source"], "page": int(item["page"]), "score": float(score)})
    return results
