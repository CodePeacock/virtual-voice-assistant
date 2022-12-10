import sys
from email.mime import audio
from fileinput import filename
from turtle import done

import pyttsx3 as tts
import speech_recognition
from neuralintents import GenericAssistant


def init():
    """
    This function initializes the speech recognizer, the text-to-speech engine, and the to-do list
    :return: the recognizer, speaker, and todo_list.
    """
    recognizer = speech_recognition.Recognizer()

    speaker = tts.init()
    speaker.setProperty("rate", 150)

    todo_list = ["Go Shopping", "Clean Room", "Record Video", "Play Badminton"]
    return recognizer, speaker, todo_list


recognizer, speaker, todo_list = init()


def create_note():
    """
    It creates a note with a filename and a note.
    """
    global recognizer

    speaker.say("What do you want to write onto your note?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Choose a filename!")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(f"{filename}.txt", "w") as f:
                f.write(note)
                done = True
                speaker.say(f"I successfully created the note {filename}")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand you! Please try agian!")
            speaker.runAndWait()


def add_todo():
    """
    It asks the user what they want to add to their todo list, and then it adds it to the todo list
    """
    global recognizer

    speaker.say("What todo do you want to add?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                todo = recognizer.recognize_google(audio)
                todo = todo.lower()

                todo_list.append(todo)
                done = True
                speaker.say(f"I successfully added {todo} to your todo list")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand you! Please try agian!")
            speaker.runAndWait()


def show_todo():
    """
    The function `show_todo()` will say "Here is your todo list" and then say each item in the
    `todo_list` one by one
    """
    speaker.say("Here is your todo list")
    speaker.runAndWait()

    for todo in todo_list:
        speaker.say(todo)
        speaker.runAndWait()


def hello():
    """
    The function `hello()` uses the `say()` method of the `speaker` object to say "Hello!. What can I do
    for you?" and then uses the `runAndWait()` method of the `speaker` object to run the `say()` method
    """
    speaker.say("Hello!. What can I do for you?")
    speaker.runAndWait()


def quit():
    """
    It says "Goodbye!" and then exits the program
    """
    speaker.say("Goodbye!")
    speaker.runAndWait()
    sys.exit()


mappings = {
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todo": show_todo,
    "greeting": hello,
    "exit": quit,
}


def model_train_save(mappings):
    """
    It takes a dictionary of intent names and functions, and returns a trained and saved model

    :param mappings: a dictionary of intent names to functions that handle the intent
    :return: The assistant object
    """
    assistant = GenericAssistant("intents.json", intent_methods=mappings)
    assistant.train_model()
    assistant.save_model(model_name="EVA")
    # assistant.request("Who are you?")
    assistant.load_model(model_name="EVA")
    return assistant


assistant = model_train_save(mappings)

# Listening for the user to say something, and then it is trying to recognize what the user said. If
# it can't recognize what the user said, it will say "I did not understand you! Please try agian!"
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()

            # print(message)

            # if message == "exit":
            #     sys.exit()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        speaker.say("I did not understand you! Please try agian!")
        speaker.runAndWait()

    except speech_recognition.RequestError:
        recognizer = speech_recognition.Recognizer()
        speaker.say("I did not understand you! Please try agian!")
        speaker.runAndWait()

    except speech_recognition.WaitTimeoutError:
        recognizer = speech_recognition.Recognizer()
        speaker.say("I did not understand you! Please try agian!")
        speaker.runAndWait()
