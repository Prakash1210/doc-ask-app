# main.py
import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from embed_store import store
from utils import extract_text_from_pdf, chunk_text, make_metadata_for_chunks
from pydantic import BaseModel
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    ext = file.filename.split(".")[-1].lower()
    if ext not in ("pdf", "txt", "md"):
        raise HTTPException(status_code=400, detail="Only PDF/TXT/MD supported in this example.")
    tmp_path = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(tmp_path, "wb") as f:
        f.write(await file.read())
    if ext == "pdf":
        text = extract_text_from_pdf(tmp_path)
    else:
        text = open(tmp_path, "r", encoding="utf-8").read()
    chunks = chunk_text(text)
    metas = make_metadata_for_chunks(file.filename, chunks)
    store.add_documents(chunks, metas)
    return {"status": "ok", "chunks": len(chunks)}

@app.post("/ask")
async def ask(req: AskRequest):
    q = req.question
    # 1) find relevant chunks using FAISS
    results = store.query(q, top_k=5)
    context = "\n\n---\n\n".join([r[0]["text"] for r in results])
    # 2) call chat completion with context
    prompt = f"""You are a helpful assistant. Use the following context from uploaded documents to answer the question. If the context doesn't contain the answer, say you don't know.

CONTEXT:
{context}

QUESTION:
{q}

Answer concisely and cite the document filename when appropriate.
"""
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        max_tokens=512,
    )
    answer = resp.choices[0].message.content
    return {"answer": answer, "sources": [r[0]["doc"] for r in results]}

@app.get("/")
async def root():
    return {"status": "running"}
