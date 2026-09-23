import json
import unittest
from src.retrieval import retrieve_context
from src.vector_store import VectorStore

class TestRetrieval(unittest.TestCase):
    def setUp(self):
        self.vector_store = VectorStore()
        self.load_test_data()

    def load_test_data(self):
        # Load good retrieval example
        with open('data/examples/good_retrieval.json') as f:
            self.good_retrieval_data = json.load(f)
            for item in self.good_retrieval_data['embeddings']:
                self.vector_store.add_embeddings(item['embedding'], item['context'])

        # Load bad retrieval example
        with open('data/examples/bad_retrieval.json') as f:
            self.bad_retrieval_data = json.load(f)

    def test_good_retrieval(self):
        query = self.good_retrieval_data['query']
        expected_context = self.good_retrieval_data['expected_context']
        retrieved_context = retrieve_context(query, self.vector_store)
        self.assertIn(expected_context, retrieved_context)

    def test_bad_retrieval(self):
        query = self.bad_retrieval_data['query']
        expected_context = self.bad_retrieval_data['expected_context']
        retrieved_context = retrieve_context(query, self.vector_store)
        self.assertNotIn(expected_context, retrieved_context)

if __name__ == '__main__':
    unittest.main()