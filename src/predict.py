from src.preprocess import load_data
from src.ngram_model import NGramModel
from src.autocorrect import AutoCorrect

tokens = load_data("data/corpus.txt")

ngram = NGramModel(3)
ngram.train(tokens)

auto = AutoCorrect()

def get_prediction(text):
    corrected = auto.correct(text)
    suggestions = ngram.predict(corrected)
    return corrected, suggestions