import os
import json
import faiss
import fitz  # PyMuPDF
import docx
from sentence_transformers import SentenceTransformer

def extract_text_from_pdf(path):
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def split_into_chunks(text, chunk_size=500):
    sentences = text.split(". ")
    chunks = []
    current = ""
    for sentence in sentences:
        if len(current) + len(sentence) < chunk_size:
            current += sentence + ". "
        else:
            chunks.append(current.strip())
            current = sentence + ". "
    if current:
        chunks.append(current.strip())
    return chunks

def process_documents(doc_folder="docs"):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    all_chunks = []
    vectors = []

    for filename in os.listdir(doc_folder):
        path = os.path.join(doc_folder, filename)
        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(path)
        elif filename.endswith(".docx"):
            text = extract_text_from_docx(path)
        else:
            continue

        chunks = split_into_chunks(text)
        for idx, chunk in enumerate(chunks):
            all_chunks.append({
                "text": chunk,
                "source": filename,
                "chunk_id": idx
            })
            vectors.append(chunk)

    embeddings = model.encode(vectors)
    index = faiss.IndexFlatL2(384)
    index.add(embeddings)

    # Save index
    faiss.write_index(index, "vector_store/faiss.index")

    # Save metadata
    with open("vector_store/metadata.json", "w") as f:
        json.dump(all_chunks, f, indent=2)

    print(f"Processed {len(all_chunks)} chunks from {len(os.listdir(doc_folder))} files.")

if __name__ == "__main__":
    process_documents()
