import faiss
import numpy as np
import pickle
import os

class SimpleVectorStore:
    """A lightweight FAISS wrapper to avoid DLL issues."""
    def __init__(self, dimension: int = 1536): # 1536 for OpenAI embeddings
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = []

    def add(self, vector: np.ndarray, text: str, meta: dict):
        self.index.add(vector.astype('float32'))
        self.metadata.append({"text": text, "meta": meta})

    def search(self, query_vector: np.ndarray, k: int = 3):
        distances, indices = self.index.search(query_vector.astype('float32'), k)
        results = []
        for i in indices[0]:
            if i != -1:
                results.append(self.metadata[i])
        return results