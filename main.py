from extract_pdf_text import extract_pdf_text
from query_ollama import query_ollama

pdf_path = "Manual_de_usuario_WH 7054.pdf"
document = extract_pdf_text(pdf_path)

question = "Como instalar el calentador"
prompt = f"""Ayuda con ...

DOCUMENT:
{document[:3000]}  # You may need to chunk large PDFs

QUESTION:
{question}
"""

response = query_ollama(prompt)
print("\nAI Response:\n", response)
