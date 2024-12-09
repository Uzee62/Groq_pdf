from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import streamlit as st

def initialize_llm(api_key):
    return ChatGroq(api_key=api_key, model_name="Llama3-8b-8192")

def generate_response(llm, prompt1, language, words):
    if prompt1 and "vectors" in st.session_state:
        
        document_chain = create_stuff_documents_chain(llm, get_prompt_template())
        retriever = st.session_state.vectors.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        
        response = retrieval_chain.invoke({
            'input': prompt1,
            'words': words,
            'language': language
        })
            
        st.session_state.response = response['answer']

def get_prompt_template():
    return ChatPromptTemplate.from_template(
        """
        Answer the questions based on the provided context only.
        Please provide the most accurate response in {language} only.
        
        The response should contain exactly {words} words or as close to it as possible.
        <context>
        {context}
        <context>
        Questions: {input}
        """
    )
