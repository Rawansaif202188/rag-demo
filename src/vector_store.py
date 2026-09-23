import numpy as np


class VectorStore:
    def __init__(self):
        self.documents = []
        self.embeddings = []

    def add_embeddings(self, documents, embeddings):
        if len(documents) != len(embeddings):
            raise ValueError("documents and embeddings must be the same length.")

        self.documents.extend(documents)
        self.embeddings.extend(embeddings)

    def search(self, query_embedding, top_k=3):
        if not self.documents:
            raise ValueError("Vector store is empty.")

        doc_embeddings = np.array(self.embeddings, dtype=float)
        query = np.array(query_embedding, dtype=float)

        norms = np.linalg.norm(doc_embeddings, axis=1) * np.linalg.norm(query)
        similarities = (doc_embeddings @ query) / norms

        top_indices = np.argsort(similarities)[::-1][:top_k]
        return [(self.documents[i], float(similarities[i])) for i in top_indices]