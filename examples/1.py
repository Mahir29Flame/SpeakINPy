from speakinpy import transcribe
import os

API_KEY = os.environ.get("GROQ_API_KEY")
audio_path = "samples/audio.wav"

text = transcribe(API_KEY, audio_path)
print(text)