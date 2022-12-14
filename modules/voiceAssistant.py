import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

vaname = "Alice"


def speak(audio):
    """
    The function takes in a string of text, converts it to speech, and plays it back to the user

    :param audio: The audio to be played
    """
    engine.say(audio)
    engine.runAndWait()


def fine_tune_audio(r, source):
    # r.adjust_for_ambient_noise(source, duration=1)
    print("Listening...")
    r.pause_threshold = 1
    result = r.listen(source)
    print("Now you can speak...")

    return result


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = fine_tune_audio(r, source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query
