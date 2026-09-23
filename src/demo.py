from chunking import chunk_documents
from embeddings import generate_embeddings
from vector_store import VectorStore
from retrieval import retrieve_context
from llm import generate_response
import json

def load_documents():
    documents = []
    with open('data/documents/product_manual.md', 'r') as file:
        documents.append(file.read())
    with open('data/documents/faq.md', 'r') as file:
        documents.append(file.read())
    with open('data/documents/support_guide.md', 'r') as file:
        documents.append(file.read())
    return documents

def run_rag_pipeline(example):
    documents = load_documents()
    chunks = chunk_documents(documents)
    embeddings = generate_embeddings(chunks)
    
    vector_store = VectorStore()
    vector_store.add_embeddings(embeddings)

    query = example['query']
    retrieved_context = retrieve_context(query, vector_store)
    
    response = generate_response(retrieved_context)
    return response

def main():
    with open('data/examples/good_retrieval.json', 'r') as file:
        good_example = json.load(file)
    
    with open('data/examples/bad_retrieval.json', 'r') as file:
        bad_example = json.load(file)

    print("Good Retrieval Example:")
    good_response = run_rag_pipeline(good_example)
    print(good_response)

    print("\nBad Retrieval Example:")
    bad_response = run_rag_pipeline(bad_example)
    print(bad_response)

if __name__ == "__main__":
    main()