# RAG Pipeline Prototype

An educational prototype that demonstrates the core architecture and data flow of a Retrieval-Augmented Generation (RAG) pipeline using simplified and mocked components.

This project is designed for learning and experimentation. It does **not** use a real Large Language Model (LLM) or a production-grade embedding model.

## Pipeline

```text
Documents
    ↓
Document Chunking
    ↓
Mock Embeddings
    ↓
Vector Store
    ↓
Similarity Retrieval
    ↓
Retrieved Context
    ↓
Simulated Response Generation
```

## Project Structure

```text
rag-demo/
├── data/
│   ├── documents/
│   └── examples/
├── src/
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieval.py
│   ├── generation.py
│   └── demo.py
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## Components

### 1. Document Chunking

Documents are split into smaller text chunks to prepare them for retrieval.

Implemented in:

```text
src/chunking.py
```

### 2. Mock Embeddings

The project uses a simplified fixed-dimensional vector representation to demonstrate the concept of embeddings.

This is **not a semantic embedding model**.

Implemented in:

```text
src/embeddings.py
```

### 3. Vector Store

A simple in-memory vector store is implemented using NumPy.

It uses cosine similarity to compare the query vector with stored document vectors.

Implemented in:

```text
src/vector_store.py
```

### 4. Retrieval

The retrieval component generates a mock embedding for the user's query and retrieves the most similar document chunks.

Implemented in:

```text
src/retrieval.py
```

### 5. Simulated Generation

The generation component combines the retrieved context into a simulated response.

No real language model is used.

Implemented in:

```text
src/generation.py
```

## Running the Project

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the demo:

```bash
python src/demo.py
```

Enter a question when prompted.

The system will:

1. Load the documents.
2. Split them into chunks.
3. Generate mock embeddings.
4. Store the embeddings.
5. Retrieve the most similar chunks.
6. Display the retrieved context.
7. Generate a simulated response.

## Educational Scope

This project is intentionally implemented as a simplified RAG pipeline prototype.

The following components are mocked or simplified:

* Embeddings are generated using a basic character-based representation.
* Vector storage is implemented using NumPy.
* Response generation is simulated.
* No real LLM API is used.
* No production vector database is used.
* Retrieval quality is intentionally limited compared with semantic embedding models.

The goal is to understand the architecture and data flow of a RAG pipeline before introducing production-grade embedding models, vector databases, and LLM APIs.

## Limitations

Because this project uses simplified mock components, retrieved results may not always be semantically relevant to the user's question.

This behavior is intentional and demonstrates why real RAG systems require semantic embeddings and more advanced retrieval techniques.

## License

This project is provided for educational and learning purposes.
