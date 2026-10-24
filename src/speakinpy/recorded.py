from google import genai
import os

def transcribe(audio_path:str, GEMINI_API_KEY:str):
    MODEL_ID = "gemini-3.5-transcribe"
    client = genai.Client(api_key=GEMINI_API_KEY)
    audio_file = client.files.upload(file=audio_path)

    interaction = client.interactions.create(
        model=MODEL_ID,
        input=[{"type": "audio", "uri": audio_file.uri}],
    )

    return interaction.output_text

if __name__ == "__main__":
    GEMINI_API_KEY=os.environ.get("GEMINI_API_KEY")
    audio_path = input("Enter the local audio file path: ").strip().strip('"')
    print(transcribe(audio_path, GEMINI_API_KEY))