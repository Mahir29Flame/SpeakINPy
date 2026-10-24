# SpeakINPy
A python module for transcribing audio files to text via Google GenAI

## Installation
```bash
pip install SpeakINPy
```
or via UV:
```bash
uv add SpeakINPy
```

## Usage
```python
from speakinpy import transcribe
import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
audio_path = "path/to/audio.m4a"

text = transcribe(audio_path, GEMINI_API_KEY)
print(text)
```