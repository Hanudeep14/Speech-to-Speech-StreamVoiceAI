import requests
from config import ELEVENLABS_API_KEY, VOICE_ID

def text_to_speech(text, filename="output.mp3"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    body = {
        "text": text,
        "model_id": "eleven_monolingual_v1"
    }
    response = requests.post(url, headers=headers, json=body)
    with open(filename, "wb") as f:
        f.write(response.content)
    return filename
