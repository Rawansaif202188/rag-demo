from src.app import run_rag_pipeline
import json

def test_good_retrieval():
    with open('data/examples/good_retrieval.json') as f:
        example = json.load(f)
    
    query = example['query']
    expected_response = example['expected_response']
    
    response = run_rag_pipeline(query)
    
    assert response == expected_response, f"Expected: {expected_response}, but got: {response}"

def test_bad_retrieval():
    with open('data/examples/bad_retrieval.json') as f:
        example = json.load(f)
    
    query = example['query']
    expected_response = example['expected_response']
    
    response = run_rag_pipeline(query)
    
    assert response == expected_response, f"Expected: {expected_response}, but got: {response}"