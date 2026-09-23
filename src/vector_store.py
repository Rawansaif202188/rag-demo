import numpy as np


class VectorStore:
    """
    Simple in-memory vector store for educational purposes.
    """

    def __init__(self):
        self.documents = []
        self.embeddings = []

    def add_embeddings(self, documents, embeddings):
        """
        Store documents and their corresponding embeddings.
        """

        self.documents.extend(documents)
        self.embeddings.extend(embeddings)

    def search(self, query_embedding, top_k=3):
        """
        Retrieve the most similar documents using cosine similarity.
        """

        if not self.embeddings:
            return []

        doc_embeddings = np.array(self.embeddings, dtype=float)
        query = np.array(query_embedding, dtype=float)

        query_norm = np.linalg.norm(query)

        if query_norm == 0:
            return []

        doc_norms = np.linalg.norm(doc_embeddings, axis=1)

        similarities = np.zeros(len(doc_embeddings))

        valid = doc_norms > 0

        similarities[valid] = (
            doc_embeddings[valid] @ query
        ) / (
            doc_norms[valid] * query_norm
        )

        top_indices = np.argsort(similarities)[::-1][:top_k]

        return [
            (self.documents[i], float(similarities[i]))
            for i in top_indices
        ]