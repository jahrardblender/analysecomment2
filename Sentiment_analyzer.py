from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from transformers import pipeline

from tensorflow.keras import backend as K
import gc

class Sentiment_analyzer:
    def __init__(self, model_path = "./pretrained_models/sentiment_analysis/", threshold = 0.5):
        self.threshold = threshold # If the score of a comment is below this threshold, it is considered neutral

        self.tokenizer = AutoTokenizer.from_pretrained("./pretrained_models/sentiment_analysis/")
        self.model = TFAutoModelForSequenceClassification.from_pretrained("./pretrained_models/sentiment_analysis/")

        self.nlp = pipeline('sentiment-analysis', model = self.model, tokenizer = self.tokenizer)

    def predict(self, comment):
        pred = self.nlp(comment)[0]
        label = pred["label"]
        score = pred["score"]

        if score < self.threshold:
            label = "NEUTRAL"

        return label, score

    def clean_session(self):
        K.clear_session()
        del self.model
        del self.tokenizer
        del self.nlp
        gc.collect()
