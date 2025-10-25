# utils.py
import fitz  # PyMuPDF
import uuid
import math

def extract_text_from_pdf(path: str) -> str:
    doc = fitz.open(path)
    text = []
    for page in doc:
        text.append(page.get_text().strip())
    return "\n\n".join(text)

def chunk_text(text: str, chunk_size: int = 800, overlap: int = 200):
    # naive chunker by characters
    chunks = []
    start = 0
    length = len(text)
    while start < length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
        if start < 0:
            start = 0
    return chunks

def make_metadata_for_chunks(doc_name: str, chunks):
    metas = []
    for i, c in enumerate(chunks):
        metas.append({"doc": doc_name, "chunk_index": i, "text": c})
    return metas
