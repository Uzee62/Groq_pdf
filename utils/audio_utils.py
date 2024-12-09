from gtts import gTTS
from io import BytesIO
import streamlit as st

language_mapping = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Arabic": "ar",
    "Urdu": "ur"
}

def text_to_speech(text, language):
    lang_code = language_mapping.get(language, "en")
    try:
        tts = gTTS(text=text, lang=lang_code, slow=False)
        audio_data = BytesIO()
        tts.write_to_fp(audio_data)
        st.audio(audio_data.getvalue(), format="audio/mp3", start_time=0)
    except Exception as e:
        st.error(f"Error generating audio: {e}")
