from google import genai
import os

MODEL_ID = "gemini-3.5-transcribe"
GEMINI_API_KEY=os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

audio_path = input("Enter the local audio file path: ").strip().strip('"')

audio_file = client.files.upload(file=audio_path)

interaction = client.interactions.create(
    model=MODEL_ID,
    input=[{"type": "audio", "uri": audio_file.uri}],
)

print("Transcription result:")
print(interaction.output_text)