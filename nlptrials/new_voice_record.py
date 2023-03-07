"""This is a test of the speech recognition library. It will listen to the user's speech and tag it with part-of-speech tags."""
import logging
from typing import List, Tuple

import nltk
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)


def tag_speech(speech_text: str) -> List[Tuple[str, str]]:
    """Tag the user's speech with part-of-speech tags"""
    words = nltk.word_tokenize(speech_text)
    return nltk.pos_tag(words, tagset="universal")


with sr.Microphone() as source:
    while True:
        logging.debug("Say something!")
        audio = r.listen(source)

        # Recognize speech using Google Speech Recognition
        try:
            speech_text = r.recognize_google(audio)
            tag_speech(speech_text)
        except sr.UnknownValueError as error:
            logging.error(
                f"Google Speech Recognition could not understand audio;{error}"
            )
        except sr.RequestError as error:
            logging.error(
                f"Could not request results from Google Speech Recognition service; {error}"
            )
