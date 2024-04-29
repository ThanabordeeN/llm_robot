from transformers import pipeline
import torch

class speech_recognition:
    def __init__(self) -> None:
        MODEL_NAME = "biodatlab/whisper-th-medium-combined"  # specify the model name
        lang = "th"  # change to Thai langauge

        device = 0 if torch.cuda.is_available() else "cpu"
        self.pipe = pipeline(
            task="automatic-speech-recognition",
            model=MODEL_NAME,
            chunk_length_s=30,
            device=device,
        )
        self.pipe.model.config.forced_decoder_ids = self.pipe.tokenizer.get_decoder_prompt_ids(
        language=lang,
        task="transcribe"
        )
    def get_text(self, audio_path):
        self.text = self.pipe(audio_path)["text"]
        return self.text
    

