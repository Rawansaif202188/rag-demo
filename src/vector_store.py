class VectorStore:
    def __init__(self):
        self.embeddings = []
        self.documents = []

    def add_embeddings(self, embeddings, documents):
        self.embeddings.extend(embeddings)
        self.documents.extend(documents)

    def search(self, query_embedding, top_k=5):
        # Simple cosine similarity search
        similarities = [
            self.cosine_similarity(query_embedding, emb) for emb in self.embeddings
        ]
        top_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)[:top_k]
        return [self.documents[i] for i in top_indices]

    @staticmethod
    def cosine_similarity(vec_a, vec_b):
        dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
        norm_a = sum(a ** 2 for a in vec_a) ** 0.5
        norm_b = sum(b ** 2 for b in vec_b) ** 0.5
        return dot_product / (norm_a * norm_b) if norm_a and norm_b else 0.0