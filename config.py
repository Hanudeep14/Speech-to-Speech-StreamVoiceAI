import os
from dotenv import load_dotenv
load_dotenv()

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("VOICE_ID")
