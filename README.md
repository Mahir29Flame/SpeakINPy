# TranscribeNPy
A python module for transcribing audio files to text via Groq's Whisper-Large-v3/Whisper-Large-v3-turbo

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

text = transcribe(API_KEY, audio_path)
print(text)
```