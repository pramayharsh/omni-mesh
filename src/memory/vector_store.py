import faiss
import numpy as np
import os
import pickle
import requests
import time
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

class LibrarianStore:
    def __init__(self, index_path="data/swarm_memory.index", meta_path="data/swarm_memory.pkl"):
        self.api_key = os.getenv("HF_API_KEY")
        # Official client handles the URL routing for us
        self.client = InferenceClient(api_key=self.api_key)
        self.model_id = "sentence-transformers/all-MiniLM-L6-v2"
        
        self.dimension = 384
        self.index_path = index_path
        self.meta_path = meta_path
        
        if os.path.exists(index_path) and os.path.exists(meta_path):
            try:
                self.index = faiss.read_index(index_path)
                with open(self.meta_path, 'rb') as f:
                    self.metadata = pickle.load(f)
                print(f"📜 [Librarian] Memory Loaded: {len(self.metadata)} items.")
            except Exception as e:
                print(f"⚠️ [Librarian] Error loading index: {e}. Starting fresh.")
                self._init_fresh()
        else:
            self._init_fresh()

    def _init_fresh(self):
        self.index = faiss.IndexFlatL2(self.dimension)
        self.metadata = []
        print("📜 [Librarian] Starting fresh memory index.")

    def _get_embedding(self, text):
        """Uses official HF client for feature extraction."""
        try:
            # This calls the correct 'feature-extraction' endpoint
            embedding = self.client.feature_extraction(text, model=self.model_id)
            # HF returns a nested list/tensor; convert to a flat list
            return embedding.tolist()
        except Exception as e:
            print(f"❌ HF Client Error: {e}")
            return [0] * self.dimension

    def add_memory(self, text: str, meta: dict):
        vector = self._get_embedding(text)
        # Ensure vector is valid list of floats
        if isinstance(vector, list) and len(vector) == self.dimension:
            self.index.add(np.array([vector]).astype('float32'))
            self.metadata.append({"content": text, "meta": meta})
            
            # Save persistence
            faiss.write_index(self.index, self.index_path)
            with open(self.meta_path, 'wb') as f:
                pickle.dump(self.metadata, f)
            print(f"✅ Memorized: {text[:30]}...")

    def query(self, query_text: str, k: int = 3):
        if not self.metadata: return []
        
        query_vector = self._get_embedding(query_text)
        if not isinstance(query_vector, list): return []

        distances, indices = self.index.search(np.array([query_vector]).astype('float32'), k)
        
        results = []
        for i in indices[0]:
            if i != -1 and i < len(self.metadata):
                results.append(self.metadata[i])
        return results