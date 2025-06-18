import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import streamlit as st

def transcribe_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return None

def speak_text(text):
    tts = gTTS(text)
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
        tts.save(fp.name)
        audio_file = open(fp.name, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')