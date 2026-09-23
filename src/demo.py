from pathlib import Path

from chunking import chunk_documents
from embeddings import generate_embeddings
from vector_store import VectorStore
from retrieval import retrieve_context
from generation import generate_response


def load_documents():
    """
    Load documents from the data/documents directory.
    """

    project_root = Path(__file__).resolve().parent.parent
    documents_path = project_root / "data" / "documents"

    documents = []

    for file_path in documents_path.glob("*.md"):
        documents.append(file_path.read_text(encoding="utf-8"))

    return documents


def main():
    print("=== RAG Pipeline Prototype ===\n")

    # 1. Load documents
    documents = load_documents()
    print(f"Loaded documents: {len(documents)}")

    # 2. Split documents into chunks
    chunks = chunk_documents(documents)
    print(f"Created chunks: {len(chunks)}")

    # 3. Generate mock embeddings
    embeddings = generate_embeddings(chunks)
    print(f"Generated mock embeddings: {len(embeddings)}")

    # 4. Store documents and embeddings
    vector_store = VectorStore()
    vector_store.add_embeddings(chunks, embeddings)

    # 5. Get user query
    query = input("\nEnter your question: ")

    # 6. Retrieve relevant context
    retrieved_context = retrieve_context(
        query,
        vector_store,
        top_k=3
    )

    print("\n=== Retrieved Context ===")

    for i, (context, score) in enumerate(retrieved_context, start=1):
        print(f"\nResult {i} | Similarity: {score:.4f}")
        print(context)

    # 7. Generate simulated response
    response = generate_response(retrieved_context)

    print("\n=== Generated Response ===")
    print(response)


if __name__ == "__main__":
    main()