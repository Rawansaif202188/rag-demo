def retrieve_context(query, vector_store):
    """
    Retrieve relevant context based on the given query from the vector store.
    
    Args:
        query (str): The query string to search for.
        vector_store (VectorStore): An instance of the VectorStore class to perform the search.
    
    Returns:
        list: A list of retrieved contexts relevant to the query.
    """
    # Generate embeddings for the query
    query_embedding = generate_embeddings([query])
    
    # Search the vector store for relevant contexts
    retrieved_contexts = vector_store.search(query_embedding)
    
    return retrieved_contexts