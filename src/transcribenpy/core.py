import os
from groq import Groq

def transcribe(api_key: str, filename: str="samples/audio.wav"):
    
    client = Groq(api_key=api_key)

    # Open the audio file
    with open(filename, "rb") as file:
        # Create a transcription of the audio file
        transcription = client.audio.transcriptions.create( # API call
        file=file, # Required audio file
        model="whisper-large-v3-turbo", # Required model to use for transcription
        )
        # To print only the transcription text, you'd use print(transcription.text) (here we're printing the entire transcription object to access timestamps)
        return transcription

