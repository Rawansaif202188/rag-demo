from embeddings import generate_embeddings


def retrieve_context(query, vector_store, top_k=3):
    """
    Retrieve the most relevant contexts using mock embeddings.
    """

    query_embedding = generate_embeddings([query])[0]

    retrieved_contexts = vector_store.search(
        query_embedding,
        top_k=top_k
    )

    return retrieved_contexts