import datetime
import webbrowser
import json
import pyttsx3
import speech_recognition as sr

import pycurl
from io import BytesIO
b_obj = BytesIO()
crl = pycurl.Curl()
crl.setopt(
    crl.URL, 'https://api.trello.com/1/members/me/boards?key=db58ee5254120da35e6ae9a3e72029dd&token=216ba9bd2d7844ad5addfc84b90a796f35a73a3090772e6a57bb8d5d76aad712')
crl.setopt(crl.WRITEDATA, b_obj)
crl.perform()
crl.close()
get_body = b_obj.getvalue()
print('Output of GET request:\n%s' % get_body.decode('utf8'))
myjson = json.loads(get_body)
print("disableAt", myjson[0]["limits"]["attachments"]["perBoard"]["disableAt"])

# def takeCommand():

#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening")

#         r.pause_threshold = 0.7
#         audio = r.listen(source)

#         try:
#             print("Recognizing")

#             Query = r.recognize_google(audio, language="en-in")
#             print("the command is printed=", Query)

#         except Exception as e:
#             print(e)
#             print("Say that again sir")
#             return "None"

#         return Query


# def speak(audio):
#     """
#     It takes in a string, and then uses the pyttsx3 library to convert the string into speech

#     :param audio: The text that you want to convert to speech
#     """

#     engine = pyttsx3.init()

#     voices = engine.getProperty("voices")

#     engine.setProperty("voice", voices[0].id)

#     engine.say(audio)

#     engine.runAndWait()


# def tellDay():
#     """
#     It takes the current day of the week, and returns the name of the day of the week.
#     """

#     day = datetime.datetime.now().weekday() + 1

#     Day_dict = {
#         1: "Monday",
#         2: "Tuesday",
#         3: "Wednesday",
#         4: "Thursday",
#         5: "Friday",
#         6: "Saturday",
#         7: "Sunday",
#     }

#     if day in Day_dict:
#         day_of_the_week = Day_dict[day]
#         print(day_of_the_week)
#         speak(f"The day is {day_of_the_week}")


# def tellTime():
#     """
#     It takes the current time, converts it to a string, and then prints it
#     """

#     time = str(datetime.datetime.now())

#     print(time)
#     hour = time[11:13]
#     minutes = time[14:16]
#     speak(f"The time is {hour}Hours and{minutes}Minutes")


# def Hello():

#     speak("hello sir I am your desktop assistant. Tell me how may I help you")


# query_arr = [
#     "open geeksforgeeks",
#     "open google",
#     "open trello",
#     "which day it is",
#     "tell me the time",
#     "bye",
#     "from wikipedia",
#     "tell me your name",
# ]


# def Take_query():
#     """
#     It takes the query from the user and performs the action accordingly.
#     """
#     Hello()
#     while True:
#         query = takeCommand().lower()
#         if query_arr[0] in query:
#             speak("Opening GeeksforGeeks ")

#             webbrowser.open("www.geeksforgeeks.com")
#             continue

#         elif query_arr[1] in query:
#             speak("Opening Google ")
#             webbrowser.open("www.google.com")
#             continue

#         elif query_arr[2] in query:
#             speak("Opening Trello ")
#             webbrowser.open("www.trello.com")
#             continue

#         elif query_arr[3] in query:
#             tellDay()
#             continue

#         elif query_arr[4] in query:
#             tellTime()
#             continue

#         elif query_arr[6] in query:
#             speak("Checking the wikipedia ")
#             query = query.replace("wikipedia", "")

#             result = wikipedia.summary(query, sentences=4)
#             speak("According to wikipedia")
#             speak(result)

#         elif query_arr[7] in query:
#             speak("I am Jarvis. Your desktop Assistant")

#         elif query_arr[5] in query:
#             speak("Bye. Check Out GFG for more exciting things")
#             exit()


# if __name__ == "__main__":
#     Take_query()
