import asyncio
import websockets
import base64
import json
import pyaudio
from config import DEEPGRAM_API_KEY

async def stream_audio(callback):
    async with websockets.connect(
        f"wss://api.deepgram.com/v1/listen?punctuate=true",
        extra_headers={"Authorization": f"Token {DEEPGRAM_API_KEY}"},
    ) as ws:

        def callback_wrapper(audio_data):
            asyncio.create_task(ws.send(audio_data))

        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

        async def receive_transcript():
            while True:
                message = await ws.recv()
                data = json.loads(message)
                if 'channel' in data and 'alternatives' in data['channel']:
                    transcript = data['channel']['alternatives'][0]['transcript']
                    if transcript:
                        callback(transcript)

        await asyncio.gather(receive_transcript())

def start_transcription(callback):
    asyncio.run(stream_audio(callback))
