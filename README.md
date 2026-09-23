# RAG Demo Project

This project demonstrates the Retrieval-Augmented Generation (RAG) pipeline, which combines document retrieval and language model generation to provide contextually relevant responses. The pipeline consists of several components, including document chunking, embedding generation, vector storage, context retrieval, and response generation.

## Project Structure

```
rag-demo
├── data
│   ├── documents
│   │   ├── product_manual.md
│   │   ├── faq.md
│   │   └── support_guide.md
│   └── examples
│       ├── good_retrieval.json
│       └── bad_retrieval.json
├── src
│   ├── __init__.py
│   ├── app.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieval.py
│   ├── llm.py
│   └── demo.py
├── tests
│   ├── test_chunking.py
│   ├── test_retrieval.py
│   └── test_pipeline.py
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── .vscode
    └── settings.json
```

## Components

1. **Document Loading**: The documents are stored in the `data/documents` directory and include a product manual, FAQ, and support guide.

2. **Chunking**: The `chunking.py` module contains functions to split documents into smaller, manageable chunks for processing.

3. **Embeddings**: The `embeddings.py` module generates embeddings for the text chunks, which are essential for vector search.

4. **Vector Store**: The `vector_store.py` module manages the storage and retrieval of embeddings, allowing for efficient searching of relevant chunks.

5. **Retrieval**: The `retrieval.py` module retrieves context based on a user query, utilizing the vector store to find the most relevant information.

6. **Language Model Interaction**: The `llm.py` module interfaces with a language model to generate responses based on the retrieved context.

7. **Demo**: The `demo.py` module ties together the entire RAG pipeline, showcasing both successful and unsuccessful retrieval scenarios.

## Usage

1. **Setup**: Clone the repository and install the required dependencies listed in `requirements.txt`.

2. **Run the Application**: Execute the `app.py` file to initialize the RAG pipeline and see it in action.

3. **Testing**: Unit tests are provided in the `tests` directory to ensure the functionality of each component.

## Examples

- **Good Retrieval**: An example of a successful retrieval scenario is provided in `data/examples/good_retrieval.json`.
- **Bad Retrieval**: An example of a failed retrieval scenario is provided in `data/examples/bad_retrieval.json`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.