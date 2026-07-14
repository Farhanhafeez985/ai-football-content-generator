# app/tools/deepgram_tts.py

from pathlib import Path

from deepgram import DeepgramClient
from langchain.tools import tool

from app.config import settings


client = DeepgramClient(api_key=settings.DEEPGRAM_API_KEY)


@tool
def deepgram_tts(
    text: str,
    output_file: str = "outputs/audio/script.mp3",
    model: str = "aura-2-thalia-en",
) -> str:
    """
    Convert text into speech using Deepgram Aura TTS.
    Saves generated audio as an mp3 file.
    """

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    response = client.speak.v1.audio.generate(
        text=text,
        model=model,
    )

    with open(output_path, "wb") as audio_file:
        for chunk in response:
            audio_file.write(chunk)

    return str(output_path)