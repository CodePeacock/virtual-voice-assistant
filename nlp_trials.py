import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))


def remove_stopwords(text):
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if w not in stop_words]
    return " ".join(filtered_sentence)


def remove_punctuation(text):
    punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
    no_punct = ""
    for char in text:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct


def seperate_words(text):
    return text.split(" ")


def filter_board_name(text):
    return text.split("the board called")[1]


print(seperate_words("Add a card to the board in the list called ToDo"))
print(remove_punctuation("Add a card to the board? in the list called ToDo!"))
print(remove_stopwords("Add a card to the board in the list called ToDo"))
print(filter_board_name("Add a card to the board called ToDo"))
