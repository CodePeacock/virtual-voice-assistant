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
    engine.say(audio)
    engine.runAndWait()


# def fine_tune_audio(r, source):
#     # r.adjust_for_ambient_noise(source, duration=1)
#     print("Listening...")
#     r.pause_threshold = 1
#     r.energy_threshold = 300
#     result = r.listen(r, source)
#     print("Now you can speak...")

#     return result


def takeCommand():
    """
    It takes a command from the user, and returns it as a string
    :return: A string
    """

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 10
        print("Now you can speak...")
        audio = r.listen(r, source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query
