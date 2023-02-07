""" This file contains the functions that are used to convert text to speech and vice versa"""
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


r = sr.Recognizer()


def speak(audio):
    """
    The function takes in a string of text, converts it to speech, and plays it back to the user

    :param audio: The audio to be played
    """
    engine.say(audio, name="Microsoft Zira Desktop - English (United States)")
    engine.runAndWait()


# def fine_tune_audio(r, source):
#     # r.adjust_for_ambient_noise(source, duration=1)
#     print("Listening...")
#     r.pause_threshold = 1
#     r.energy_threshold = 300
#     result = r.listen(r, source)
#     print("Now you can speak...")

#     return result


def takecommand():
    # sourcery skip: extract-method, inline-immediately-returned-variable
    """
    It takes a command from the user, and returns it as a string
    :return: A string
    """

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        # r.energy_threshold = 10
        r.energy_threshold = 300
        print("Now you can speak...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"User said: {query}\n")

    except sr.RequestError as exception:
        print(exception)
        print("Unable to Recognize your voice.")
        return "None"
    return query
