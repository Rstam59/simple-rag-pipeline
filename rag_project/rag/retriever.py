import numpy as np
import faiss

class Retriever:
    def __init__(self, embeddings, documents):
        self.embeddings = np.array(embeddings)  # ✅ Add this
        self.documents = documents
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)


    def retrieve(self, query_embedding, top_k=3):
        distances, indices = self.index.search(np.array([query_embedding]), top_k)
        return [self.documents[i] for i in indices[0]]

