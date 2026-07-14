from app.tools.deepgram_tts import deepgram_tts


class VoiceAgent:
    """
    Converts the approved script narration into speech.
    """

    def run(self, narration: str) -> str:
        """
        Generate an MP3 from the narration.

        Returns:
            Path to the generated audio file.
        """

        audio_path = deepgram_tts.invoke(
            {
                "text": narration,
            }
        )

        return audio_path