# embed_store.py
import os
import faiss
import pickle
from typing import List, Tuple
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

EMBED_DIM = 1536  # for text-embedding-3-small / text-embedding-3-large adjust accordingly
INDEX_PATH = "faiss_index.bin"
META_PATH = "meta_store.pkl"

class EmbedStore:
    def __init__(self, dim=EMBED_DIM):
        self.dim = dim
        self.index = None
        self.metadatas = []  # list of dicts per vector
        self._load()

    def _load(self):
        if os.path.exists(INDEX_PATH) and os.path.exists(META_PATH):
            self.index = faiss.read_index(INDEX_PATH)
            with open(META_PATH, "rb") as f:
                self.metadatas = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(self.dim)
            self.metadatas = []

    def _save(self):
        faiss.write_index(self.index, INDEX_PATH)
        with open(META_PATH, "wb") as f:
            pickle.dump(self.metadatas, f)

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        # Use OpenAI embeddings API
        resp = client.embeddings.create(model="text-embedding-3-small", input=texts)
        embeddings = [r.embedding for r in resp.data]
        return embeddings

    def add_documents(self, chunks: List[str], metadatas: List[dict]):
        embeds = self.embed_texts(chunks)
        import numpy as np
        vecs = np.array(embeds).astype("float32")
        self.index.add(vecs)
        self.metadatas.extend(metadatas)
        self._save()

    def query(self, q: str, top_k: int = 4) -> List[Tuple[dict, float]]:
        q_emb = self.embed_texts([q])[0]
        import numpy as np
        q_vec = np.array([q_emb]).astype("float32")
        D, I = self.index.search(q_vec, top_k)
        results = []
        for dist, idx in zip(D[0], I[0]):
            if idx < len(self.metadatas):
                results.append((self.metadatas[idx], float(dist)))
        return results

store = EmbedStore()
