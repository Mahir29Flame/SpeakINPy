# TranscribeNPy
A python module for transcribing audio files to text via Groq's Whisper-Large-v3/Whisper-Large-v3-turbo\
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/transcribenpy?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=Downloads)](https://pepy.tech/projects/transcribenpy)

## Installation
```bash
pip install TranscribeNPy
```
or via UV:
```bash
uv add TranscribeNPy
```

## Usage
```python
from transcribenpy import transcribe
import os

API_KEY = os.environ.get("GROQ_API_KEY")
audio_path = "samples/audio.wav"

text = transcribe(API_KEY, audio_path, model="Precise")
print(text)
```

## Parameters

- `api_key` : String
    - Groq API Key
    - Required
- `filename` : String
    - Audio file path
    - Default: "samples/audio.wav"
- `model` : String
    - Model to use for transcription
    - Options: 
      - "Fast" / "Quick" / "Fastest" / "Turbo" -> "whisper-large-v3-turbo"
      - "Precise" / "Heavy" / "Slow" -> "whisper-large-v3"
    - Default: "Fast"
