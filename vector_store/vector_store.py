from langchain_community.vectorstores.chroma import Chroma
import streamlit as st



def create_vector_store():
    try:
        vector_store=Chroma(
            collection_name="medical_reports",
            embedding_function=None,
            persist_directory="./vector_store/db",
        )
    except Exception as e:
        st.error(f"Error creating vector store: {e}")
        return None
    return vector_store