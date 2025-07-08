import os
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

PDF_DIR = "pdfs"

def extract_and_chunk_pdfs():
    docs = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    for filename in os.listdir(PDF_DIR):
        if filename.endswith(".pdf"):
            path = os.path.join(PDF_DIR, filename)
            with pdfplumber.open(path) as pdf:
                text = "\n".join(page.extract_text() or "" for page in pdf.pages)
                for chunk in splitter.split_text(text):
                    docs.append(Document(page_content=chunk, metadata={"source": filename}))
    return docs


