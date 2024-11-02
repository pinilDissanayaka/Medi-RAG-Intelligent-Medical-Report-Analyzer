import streamlit as st

st.set_page_config(page_title="Medi-RAG-Intelligent-Medical-Report-Analyzer", 
                   page_icon="🩺", 
                   layout="centered")


with st.sidebar:    
    uploaded_file=st.file_uploader("Upload Medical Report",type=['pdf'])
    