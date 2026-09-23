import unittest
from src.chunking import chunk_documents

class TestChunking(unittest.TestCase):

    def test_chunking_basic(self):
        documents = [
            "This is the first document. It has some text.",
            "This is the second document. It also has text."
        ]
        expected_chunks = [
            "This is the first document. It has some text.",
            "This is the second document. It also has text."
        ]
        chunks = chunk_documents(documents)
        self.assertEqual(chunks, expected_chunks)

    def test_chunking_empty_document(self):
        documents = [""]
        expected_chunks = [""]
        chunks = chunk_documents(documents)
        self.assertEqual(chunks, expected_chunks)

    def test_chunking_large_document(self):
        documents = [
            "This is a large document that should be chunked into smaller pieces. " * 10
        ]
        expected_chunks = [
            "This is a large document that should be chunked into smaller pieces. " * 10
        ]
        chunks = chunk_documents(documents)
        self.assertEqual(chunks, expected_chunks)

    def test_chunking_with_special_characters(self):
        documents = [
            "This document contains special characters! @#$%^&*()"
        ]
        expected_chunks = [
            "This document contains special characters! @#$%^&*()"
        ]
        chunks = chunk_documents(documents)
        self.assertEqual(chunks, expected_chunks)

if __name__ == '__main__':
    unittest.main()