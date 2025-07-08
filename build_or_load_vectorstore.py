import os
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

from extract_and_chunk_pdfs import extract_and_chunk_pdfs

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
CHROMA_DIR = "chroma_db"


def build_or_load_vectorstore():
    if os.path.exists(CHROMA_DIR) and os.listdir(CHROMA_DIR):
        print("[✓] Loading existing Chroma vector store...")
        return Chroma(persist_directory=CHROMA_DIR, embedding_function=embedding_model)
    else:
        print("[+] Building new vector store from PDFs...")
        documents = extract_and_chunk_pdfs()
        vs = Chroma.from_documents(documents, embedding_model, persist_directory=CHROMA_DIR)
        vs.persist()
        return vs