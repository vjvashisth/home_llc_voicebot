import streamlit as st
from voice_utils import transcribe_audio, speak_text
from gpt_agent import get_personalized_response

st.set_page_config(page_title="Home.LLC Voicebot", page_icon="🎙️")
st.title("🎙️ AI Voicebot for Home.LLC Interview")
st.markdown("""
Ask a question from the list or try your own:
- What should we know about your life story?
- What’s your #1 superpower?
- What are the top 3 areas you’d like to grow in?
- What misconception do your coworkers have about you?
- How do you push your boundaries?
""")

st.info("🎙️ Mic input is supported in the local version. This demo uses text input for cloud compatibility.")

question = st.text_input("Type your question here:")

if question:
    with st.spinner("Generating response..."):
        answer = get_personalized_response(question)
    st.markdown(f"**Answer:** {answer}")
    speak_text(answer)
