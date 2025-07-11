FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .

# Minimal system deps to build faiss
RUN apt-get update && apt-get install -y gcc libglib2.0-0 && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir faiss-cpu==1.7.4 && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y gcc && apt-get autoremove -y && apt-get clean

COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
