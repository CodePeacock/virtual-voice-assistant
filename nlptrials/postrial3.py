"""This program will tokenize the text and then tag each word with a part of speech"""
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
SAMPLE_TEXT = "I want to add a new card named test one to the list named test list in board named test board."

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(SAMPLE_TEXT)


def process_content():
    """This function will tokenize the text and then tag each word with a part of speech"""
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            print(tagged)

    except Exception() as exception:
        print(exception)
        raise


process_content()
