import numpy as np


def generate_embeddings(chunks, dimension=64):
    """
    Generate simplified mock embeddings.

    This implementation is intentionally simple and is NOT
    a real semantic embedding model.
    """

    embeddings = []

    for chunk in chunks:
        vector = np.zeros(dimension, dtype=float)

        for char in chunk:
            index = ord(char) % dimension
            vector[index] += 1

        # Normalize the vector
        norm = np.linalg.norm(vector)

        if norm > 0:
            vector = vector / norm

        embeddings.append(vector)

    return embeddings