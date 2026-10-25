import os
from groq import Groq

def isVaild(api_key):
    if not api_key or api_key.strip() == "" or len(api_key) < 5:
        return False
    return True
    
def isFileVaild(filename):
    if (not os.path.exists(filename)) or (not os.path.isfile(filename)) or filename.strip() == "":
        return False
    return True

def getModel(model:str):
    if model.lower() == "fast" or model.lower() == "quick" or model.lower() == "fastest" or model.lower() == "turbo":
        return "whisper-large-v3-turbo"
    elif model.lower() == "precise" or model.lower() == "heavy" or model.lower() == "slow":
        return "whisper-large-v3"
    else:
        return "whisper-large-v3-turbo"

def transcribe(api_key, filename="samples/audio.wav", model="Fast"):
    if not isVaild(api_key):
        raise ValueError(f"API Key: {api_key} is invalid")
    
    if not isFileVaild(filename):
        raise ValueError(f"Audio file: {filename} is invalid")

    client = Groq(api_key=api_key)
    model = getModel(model)

    # Open the audio file
    with open(filename, "rb") as file:
        # Create a transcription of the audio file
        transcription = client.audio.transcriptions.create( # API call
        file=file, # Required audio file
        model=model, # Required model to use for transcription
        )
        # To print only the transcription text, you'd use print(transcription.text) (here we're printing the entire transcription object to access timestamps)
        return transcription

if __name__ == "__main__":
    API_KEY = os.getenv("GROQ_API_KEY")
    print(transcribe(API_KEY, "samples/audio.wav"))