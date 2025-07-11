from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils.loader import load_vector_store, search_chunks
from utils.generator import generate_answer

app = FastAPI()

# Define request body schema
class QueryRequest(BaseModel):
    query: str


@app.get("/")
def read_root():
    return {
        "message": "Welcome to Lexi Legal RAG Backend! Use the /query endpoint to get answers from legal documents."
    }


# Load FAISS index, metadata, and model once at startup

try:
    index, metadata, model = load_vector_store()
except FileNotFoundError as e:
    index = None
    metadata = []
    model = None
    print(f"[ERROR] Failed to load vector store: {e}")

@app.post("/query")
async def query(request: QueryRequest):
    if index is None or model is None:
        raise HTTPException(status_code=500, detail="Vector store or model not loaded. Please run the document loader first.")

    query_text = request.query

    # Step 1: Embed and search
    top_chunks = search_chunks(query_text, index, metadata, model)

    # Step 2: Generate answer
    answer, citations = generate_answer(query_text, top_chunks)

    return {
        "answer": answer,
        "citations": citations
    }
