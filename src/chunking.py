def chunk_documents(documents, chunk_size=100, chunk_overlap=20):
    chunks = []

    for document in documents:
        step = chunk_size - chunk_overlap

        for i in range(0, len(document), step):
            chunk = document[i:i + chunk_size]
            chunks.append(chunk)

            if i + chunk_size >= len(document):
                break

    return chunks