from sentence_transformers import SentenceTransformer
import faiss
import pickle
import json

def load_vector_store():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    with open("vector_store/metadata.json", "r") as f:
        metadata = json.load(f)
    index = faiss.read_index("vector_store/faiss.index")
    return index, metadata, model

def search_chunks(query, index, metadata, model, k=3):
    query_vec = model.encode([query])
    _, indices = index.search(query_vec, k)
    return [metadata[i] for i in indices[0]]
