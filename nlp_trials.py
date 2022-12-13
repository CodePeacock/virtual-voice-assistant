import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords")
nltk.download("punkt")

stop_words = set(stopwords.words("english"))


def remove_stopwords(text):
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if w not in stop_words]
    return " ".join(filtered_sentence)


def remove_punctuation(text):
    return text.replace(".", "").replace(",", "")
