from transformers import pipeline

from utils import exe_time


@exe_time
def speech_to_text(audio, model, token=None):
    if token:
        speech_to_text = pipeline(task="automatic-speech-recognition",
                                  model=model,
                                  use_auth_token=token,
                                  chunk_length_s=30,
                                  stride_length_s=(3, 3))
    else:
        speech_to_text = pipeline(task="automatic-speech-recognition",
                                  model=model,
                                  chunk_length_s=30,
                                  stride_length_s=(0, 0))

    b = speech_to_text(audio, max_new_tokens=9000)
    return b['text']


openas = "openai/whisper-small"
openai2 = "openai/whisper-large-v2"
facebook = "facebook/wav2vec2-base-960h"
facebook2 = "facebook/wav2vec2-large-960h-lv60-self"

r = speech_to_text(r"C:\Users\betalpha\Desktop\dump\12.mp3", openai2)
print(r)
