# import the library needed for the virtual assistant

import pyttsx3
import speech_recognition as assistance

# now, let us obtain voice input from the microphone
listener = assistance.Recognizer()

# the next line is to initiate the pttsx3 library
engine = pyttsx3.init()

# let's take voice from our microphone and use our microphone as source
with assistance.Microphone() as source:
    print("Say something...!")
    audio = listener.listen(source)

# recognize your speech using the Google Speech Recognizer
try:
    print(f"I heard you say {listener.recognize_google(audio)}")
except assistance.UnknownValueError:
    print("Hey, I could not understand what you say")
except assistance.RequestError as e:
    print("Request from Google Speech Recognition failed; {0}".format(e))

# the engine will then repeat what you said before performing your command
engine.say(audio)
engine.runAndWait()
