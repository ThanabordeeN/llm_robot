from transformers import pipeline
import torch
import os
os.environ['TRANSFORMERS_CACHE'] = r'F:/Huggingface_model/'

MODEL_NAME = "biodatlab/whisper-th-small-combined"  # specify the model name
lang = "th"  # change to Thai langauge

device = 0 if torch.cuda.is_available() else "cpu"

pipe = pipeline(
    task="automatic-speech-recognition",
    model=MODEL_NAME,
    chunk_length_s=30,
    device=device,
)
pipe.model.config.forced_decoder_ids = pipe.tokenizer.get_decoder_prompt_ids(
  language=lang,
  task="transcribe"
)
text = pipe("human.wav")["text"] # give audio mp3 and transcribe text
print(text)
