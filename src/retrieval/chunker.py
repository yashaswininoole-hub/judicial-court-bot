from langchain_text_splitters import RecursiveCharacterTextSplitter

_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1800,
    chunk_overlap=250,
    separators=["\n\n", "\n", ". ", " ", ""],
)


def chunk_pages(pages: list[dict]) -> list[dict]:
    """Split each page into passages, preserving source and PDF page."""
    chunks = []
    for page in pages:
        for text in _splitter.split_text(page["text"]):
            if text.strip():
                chunks.append({"text": text, "source": page["source"], "page": int(page["page"])})
    return chunks
