from build_or_load_vectorstore import build_or_load_vectorstore
from query_ollama import query_ollama

def retrieve_context(query, vectorstore, k=5):
    docs = vectorstore.similarity_search(query, k=k)
    return "\n\n".join(doc.page_content for doc in docs)

def chat_loop():
    vs = build_or_load_vectorstore()
    print("🤖 Hazme una pregunta (escribe 'exit' para salir):")

    while True:
        query = input("\nYou: ")
        if query.lower() in ("exit", "quit"):
            break

        context = retrieve_context(query, vs)
        prompt = f"""You are a helpful assistant. Use the context below to answer the question.

Context:
{context}

Question:
{query}
"""
        answer = query_ollama(prompt)
        print("\n🧠 DeepSeek:\n", answer)

if __name__ == "__main__":
    chat_loop()
