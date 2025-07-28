import streamlit as st
import asyncio
from deepgram import Deepgram
from config import DEEPGRAM_API_KEY
from orchestrator import build_persona_prompt
from llm_handler import get_llm_response
from tts_handler import text_to_speech

# UI Title
st.set_page_config(page_title="Voice Persona Assistant", layout="centered")
st.title("🎙️ Persona Voice Assistant (Gemini + ElevenLabs)")

# Audio Input
audio_bytes = st.file_uploader("🎧 Record or upload audio (WAV/MP3)", type=["wav", "mp3"])

# Persona Selection
persona = st.selectbox("🧠 Choose a Persona", ["Therapist", "Teacher", "Assistant"])


async def transcribe_audio(audio_data):
    dg_client = Deepgram(DEEPGRAM_API_KEY)
    response = await dg_client.transcription.prerecorded(
        {"buffer": audio_data, "mimetype": "audio/wav"},
        {"punctuate": True, "language": "en"}
    )
    return response


if audio_bytes:
    with st.spinner("🧠 Transcribing..."):
        response = asyncio.run(transcribe_audio(audio_bytes.read()))
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        st.success("✅ Transcription Complete")
        st.write("**Transcript:**", transcript)

    # Persona Prompting
    final_prompt = build_persona_prompt(transcript, persona)
    st.write("**🔧 Persona Prompt:**", final_prompt)

    # LLM Response
    with st.spinner("💡 Thinking..."):
        response_text = get_llm_response(final_prompt)
        st.write("**🤖 LLM Response:**", response_text)

    # TTS
    with st.spinner("🎤 Generating voice..."):
        audio_file_path = text_to_speech(response_text)
        audio_bytes = open(audio_file_path, "rb").read()
        st.audio(audio_bytes, format="audio/mp3")

else:
    st.info("📥 Please upload a WAV or MP3 file to begin.")
