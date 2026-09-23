from pathlib import Path
import json

from chunking import chunk_documents
from embeddings import generate_embeddings
from vector_store import VectorStore
from retrieval import retrieve_context
from llm import generate_response

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DOCS_DIR = DATA_DIR / "documents"
EXAMPLES_DIR = DATA_DIR / "examples"


def load_documents():
    if not DOCS_DIR.exists():
        raise FileNotFoundError(f"Documents folder not found: {DOCS_DIR}")

    files = sorted(DOCS_DIR.glob("*.md"))
    if not files:
        raise FileNotFoundError(f"No markdown files found in: {DOCS_DIR}")

    documents = []
    for file_path in files:
        documents.append(file_path.read_text(encoding="utf-8"))

    return documents


def load_example(file_name):
    path = EXAMPLES_DIR / file_name
    if not path.exists():
        return {"query": "What does this product do?"}

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def run_rag_pipeline(example):
    if isinstance(example, str):
        query = example
    else:
        query = example.get("query", "What does this product do?")

    documents = load_documents()
    chunks = chunk_documents(documents)
    embeddings = generate_embeddings(chunks)

    vector_store = VectorStore()
    vector_store.add_embeddings(chunks, embeddings)

    retrieved_context = retrieve_context(query, vector_store)
    response = generate_response(retrieved_context)
    return response


def main():
    good_example = load_example("good_retrieval.json")
    bad_example = load_example("bad_retrieval.json")

    print("Good Retrieval Example:")
    print(run_rag_pipeline(good_example))

    print("\nBad Retrieval Example:")
    print(run_rag_pipeline(bad_example))


if __name__ == "__main__":
    main()