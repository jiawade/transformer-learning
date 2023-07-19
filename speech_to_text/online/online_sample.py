import requests

from utils import exe_time


@exe_time
def speech_to_text_online(audio, model):
    API_URL = "https://api-inference.huggingface.co/models/" + model
    headers = {"Authorization": "Bearer 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"}
    with open(audio, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

facebook = "facebook/wav2vec2-base-960h"
speech_to_text_online(r"C:\Users\betalpha\Desktop\dump\bad.mp3", facebook)
print(speech_to_text_online)
