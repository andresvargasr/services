import streamlit as st
from build_or_load_vectorstore import build_or_load_vectorstore
from query_ollama import query_ollama

# Cargar vector store
vs = build_or_load_vectorstore()

st.set_page_config(page_title="Asistente Técnico", page_icon="🔧")
st.title("🔧 Asistente Técnico")

option = st.sidebar.radio(
    "Selecciona lo que quieres hacer:",
    ["Preguntar al Sistema", "Buscar Referencia", "Solicitar Cotización"]
)

if option == "Preguntar al Sistema":
    st.header("💬 Preguntar al Sistema")
    question = st.text_input("Escribe tu pregunta:")

    if st.button("Enviar pregunta"):
        # Búsqueda semántica en Chroma
        docs = vs.similarity_search(question, k=3)
        if docs:
            context = "\n\n".join([d.page_content for d in docs])
        else:
            context = "No se encontró contexto relevante."

        prompt = f"""
        Responde de forma técnica y clara.

        CONTEXTO:
        {context}

        PREGUNTA:
        {question}
        """

        response = query_ollama(prompt)

        st.subheader("✅ Respuesta del sistema:")
        st.write(response)

elif option == "Buscar Referencia":
    st.header("🔍 Buscar Referencia")
    ref = st.text_input("Código o referencia a buscar:")

    if st.button("Buscar"):
        # Búsqueda semántica también sirve aquí
        docs = vs.similarity_search(ref, k=5)
        if docs:
            st.success(f"Se encontraron coincidencias para: '{ref}'")
            for d in docs:
                st.write(f"**Fuente:** {d.metadata.get('source')}")
                st.write(d.page_content[:1000])
                st.write("---")
        else:
            st.warning(f"No se encontró la referencia '{ref}'.")

elif option == "Solicitar Cotización":
    st.header("💲 Solicitar Cotización")
    producto = st.text_input("Producto o referencia:")
    cantidad = st.number_input("Cantidad:", min_value=1, step=1)
    comentario = st.text_area("Comentarios adicionales:")

    if st.button("Enviar solicitud"):
        # Aquí podrías guardarlo en base de datos o enviarlo por email
        st.success(f"✅ Solicitud enviada para '{producto}' x{cantidad}.")
        st.write("Comentario:", comentario)
