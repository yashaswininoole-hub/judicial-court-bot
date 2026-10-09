from src.retrieval.chunker import chunk_pages


def test_chunk_pages_preserves_source_and_page():
    pages = [{"text": "A summons is a formal court notice.", "source": "guide.pdf", "page": 3}]
    chunks = chunk_pages(pages)
    assert chunks
    assert chunks[0]["text"] == "A summons is a formal court notice."
    assert chunks[0]["source"] == "guide.pdf"
    assert chunks[0]["page"] == 3
