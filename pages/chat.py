import streamlit as st
from langchain.memory import ConversationBufferMemory

st.set_page_config(page_title="Medi-RAG-Intelligent-Medical-Report-Analyzer", 
                   page_icon="🩺", 
                   layout="centered")


with st.sidebar:
    if "GROQ_API_KEY" in st.session_state: 
        uploaded_files=st.file_uploader("Upload Medical Report",type=['pdf'], accept_multiple_files=True)
        if uploaded_files is not None:
            if "UPLOADED_FILES" not in st.session_state.keys():
                st.session_state["UPLOADED_FILES"]=uploaded_files
    else:
        groq_api_key=st.text_input(label="GROQ API KEY", placeholder="Enter your GROQ API key", type="password")
        st.info("Please provide your GROQ API key", icon="🔒")
        st.info("You can get your API key from https://groq.com/", icon="🔑")
        
    

