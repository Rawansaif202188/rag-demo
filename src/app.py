from chunking import chunk_documents
from embeddings import generate_embeddings
from vector_store import VectorStore
from retrieval import retrieve_context
from llm import generate_response
import json
import os

def load_documents(data_dir):
    documents = []
    for filename in os.listdir(data_dir):
        if filename.endswith('.md'):
            with open(os.path.join(data_dir, filename), 'r') as file:
                documents.append(file.read())
    return documents

def main():
    # Load documents
    documents = load_documents('data/documents')

    # Chunk documents
    chunks = chunk_documents(documents)

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    # Initialize vector store and add embeddings
    vector_store = VectorStore()
    vector_store.add_embeddings(embeddings)

    # Load good retrieval example
    with open('data/examples/good_retrieval.json', 'r') as file:
        good_example = json.load(file)

    # Retrieve context for good example
    good_query = good_example['query']
    good_context = retrieve_context(good_query, vector_store)

    # Generate response for good example
    good_response = generate_response(good_context)
    print("Good Retrieval Response:", good_response)

    # Load bad retrieval example
    with open('data/examples/bad_retrieval.json', 'r') as file:
        bad_example = json.load(file)

    # Retrieve context for bad example
    bad_query = bad_example['query']
    bad_context = retrieve_context(bad_query, vector_store)

    # Generate response for bad example
    bad_response = generate_response(bad_context)
    print("Bad Retrieval Response:", bad_response)

if __name__ == "__main__":
    main()