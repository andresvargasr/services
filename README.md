# 🔍 RAG over PDFs with Chroma + DeepSeek

This is a Retrieval-Augmented Generation (RAG) pipeline that lets you ask questions about many PDF files using 
local models like DeepSeek 1.5b with Ollama.

## 🧱 Features

- PDF parsing and text chunking
- Vector search using ChromaDB
- Question answering with Ollama + DeepSeek
- 100% offline

## 🚀 Quickstart

1. Clone this repo and install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Add your PDFs to the `/pdfs` folder.

3. Run the app:
    ```bash
    python app.py
    ```

4. Ask questions like:
    ```
    Que materiales debo tener en cuenta para instalar el calentador?
    ```

## 🧠 Requirements

- Python 3.9+
- Ollama installed (`https://ollama.com`)
- Run this to download the model:
    ```bash
    ollama pull deepseek-coder:1.5b
    ```

## 📂 Vector Store

ChromaDB is used to persist the document embeddings across sessions in `/chroma_db`.

---
