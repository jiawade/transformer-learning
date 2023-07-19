from transformers import pipeline



model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"
mood = pipeline("sentiment-analysis")

v=mood("go home")
print(v)

