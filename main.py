import streamlit as st
from dotenv import load_dotenv
import os
from utils.general_utils import load_css
from utils.langchain_utils import initialize_llm, generate_response
from utils.audio_utils import text_to_speech
from preprocessing import process_pdf
import time

# Loading environment variables
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')

# Loading CSS
load_css("CSS/style.css")

#  LLM initialization
llm = initialize_llm(GROQ_API_KEY)

st.title("Let's Interact with pdf's")
st.sidebar.title("Upload your pdf files")

#Asking for Document

uploaded_files = st.sidebar.file_uploader(
    "_____________________________________", 
    type="pdf", 
    accept_multiple_files=True
)

process = st.sidebar.button("Submit")

if process:
    if uploaded_files:
        process_pdf(uploaded_files)
    else:
        st.warning("Please upload a PDF file.")

# Initializing session state
st.session_state.setdefault("response", None)
st.session_state.setdefault("last_question", None)

prompt1 = st.text_input("______", placeholder="Enter your Question")
language = st.selectbox("Choose a language", ["English", "French", "Spanish", "German", "Hindi", "Arabic", "Urdu"])
words = st.slider("Word limit for response:", 1, 500, 50)

if st.button("Respond"):
    generate_response(llm, prompt1, language, words)

if st.session_state.response:
    st.markdown(
        f"""
        <div class="card">
            <div class="response">{st.session_state.response}</div>
        </div>
        """, 
        unsafe_allow_html=True
    )

#Text to speech
if st.button("Speak"):
    message_placeholder = st.empty()  
    message_placeholder.success("Audio Loading...Please wait........")
    text_to_speech(st.session_state.response, language)
    message_placeholder.success("Audio Loaded...✅✅✅")
    time.sleep(3)  
    message_placeholder.empty() 
