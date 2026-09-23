def generate_response(context):
    """
    Simulate response generation using retrieved context.

    This is a mock generator for educational purposes.
    No real language model is used.
    """

    if not context:
        return "No relevant context found. Please refine your query."

    retrieved_text = "\n\n".join(
        document for document, _ in context
    )

    return (
        "Based on the retrieved context:\n\n"
        f"{retrieved_text}\n\n"
        "This is a simulated generated response. "
        "No real language model is used."
    )