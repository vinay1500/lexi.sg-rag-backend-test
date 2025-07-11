# Lexi RAG Backend Assignment

This is a Retrieval-Augmented Generation (RAG) backend system built with **FastAPI**. It answers legal queries using information retrieved from uploaded legal documents (PDFs or DOCX) and provides citations from the original sources.

---

## 🔧 Tech Stack

- **Backend:** FastAPI
- **Vector Store:** FAISS
- **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`)
- **Document Processing:** PyMuPDF (PDF), python-docx (DOCX)
- **Model Serving:** Open-source or mock LLM response (placeholder)

---

## 📁 Project Structure

```
lexi.sg-rag-backend-test/
│
├── main.py                   # FastAPI app with / and /query endpoints
├── requirements.txt          # Python dependencies
├── docs/                     # Place your legal PDF/DOCX files here
├── vector_store/             # Stores FAISS index and metadata
└── utils/
    ├── loader.py             # Loads vector DB and search logic
    ├── generator.py          # Answer generation logic (currently mocked)
    └── doc_loader.py         # Script to process and embed documents
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/lexi.sg-rag-backend-test.git
cd lexi.sg-rag-backend-test
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Legal Documents

Place your `.pdf` or `.docx` legal files inside the `docs/` folder.

### 4. Generate Embeddings

Run the document loader to chunk text, embed it, and save to FAISS:
```bash
python utils/doc_loader.py
```

### 5. Start the API Server

```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to use Swagger UI.

---

## 🧪 Example Request

**Endpoint:** `POST /query`  
**Body:**
```json
{
  "query": "Is an insurance company liable if a transport vehicle is used without a valid permit?"
}
```

**Response:**
```json
{
  "answer": "(Mock answer) Based on the documents...",
  "citations": [
    {
      "text": "...",
      "source": "case_law.docx"
    }
  ]
}
```

---

## ⚠️ Error Handling

If the vector store is not yet generated, `/query` will return:
```json
{
  "detail": "Vector store or model not loaded. Please run the document loader first."
}
```

---

## 🌐 Deployment (Railway)

You can deploy this easily on [Railway](https://railway.app/):

- Add a `start` script in `package.json`:
```json
{
  "scripts": {
    "start": "uvicorn main:app --host 0.0.0.0 --port $PORT"
  }
}
```

- Push to GitHub → Link Railway → Done!

---

## 📬 Contact

For any issues, email: [hi@lexi.sg](mailto:hi@lexi.sg)

---

## ✅ To-Do / Improvements

- Replace mock generator with OpenAI or local LLM
- Add frontend for document upload
- Improve citation formatting

---

© 2025 Lexi Backend Challenge – Developed by Vinay Gautam
