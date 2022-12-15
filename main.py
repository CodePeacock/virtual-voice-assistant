import os

# import wolframalpha
import datetime
import webbrowser
import pyjokes

# import requests
from twilio.rest import Client
from functions.greetUser import VANAME, username, wishMe
from functions.voiceAssistant import speak, takeCommand
from functions.voiceAssistant import *
from functions.boardFunctions import *
from functions.cardFunctions import *
from functions.listFunctions import *
from functions.cardChecklistFunctions import *

vaname = VANAME


def main(
    client,
    open_board,
    add_board,
    update_board_name,
    add_list,
    update_list_name,
    archive_list,
    add_card,
    open_card,
    update_card_name,
    delete_card,
    speak,
    takeCommand,
):
    query = takeCommand().lower()

    if "open trello" in query:
        webbrowser.open("https://trello.com/")

    elif "open board" in query:
        open_board(client)

    elif "add board" in query:
        add_board(client)

    elif "update board name" in query:
        update_board_name(client)

    elif "add list" in query:
        add_list(client)

    elif "update list name" in query:
        update_list_name(client)
    elif "archive list" in query:
        archive_list(client)

    elif "add card" in query:
        add_card(client)

    elif "open card" in query:
        open_card(client)

    elif "update card name" in query:
        update_card_name(client)

    elif "delete card" in query:
        delete_card(client)

    elif "open youtube" in query:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    elif "open google" in query:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")

    elif "open stackoverflow" in query:
        speak("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")

    # elif "play music" in query or "play song" in query:
    #     speak("Here you go with music")
    #     # music_dir = "G:\\Song"
    #     music_dir = "C:\\Users\\GAURAV\\Music"
    #     songs = os.listdir(music_dir)
    #     print(songs)
    #     random = os.startfile(os.path.join(music_dir, songs[1]))

    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("% H:% M:% S")
        speak(f"Sir, the time is {strTime}")

    elif "how are you" in query:
        speak("I am fine, Thank you")
        speak("How are you, Sir")

    elif "fine" in query or "good" in query:
        speak("It's good to know that your fine")

    elif "change my name to" in query:
        query = query.replace("change my name to", "")
        VANAME = query

    elif "change name" in query:
        speak("What would you like to call me, Sir ")
        VANAME = takeCommand()
        speak("Thanks for naming me")

    elif "what's your name" in query or "what is your name" in query:
        speak(f"My name is {vaname}")
    # print("My friends call me", VANAME)

    elif "exit" in query:
        speak("Thanks for giving me your time")
        exit()

    elif "joke" in query:
        speak(pyjokes.get_joke())
        print(pyjokes.get_joke())

    # elif "calculate" in query:
    #     app_id = "Wolframalpha api id"
    #     client = wolframalpha.Client(app_id)
    #     indx = query.lower().split().index("calculate")
    #     query = query.split()[indx + 1 :]
    #     res = client.query(" ".join(query))
    #     answer = next(res.results).text
    #     print(f"The answer is {answer}")
    #     speak(f"The answer is {answer}")

    elif "search" in query or "play" in query:
        query = query.replace("search", "")
        query = query.replace("play", "")
        webbrowser.open(query)

    # NPPR9-FWDCX-D2C8J-H872K-2YT43

    # elif "weather" in query:
    #     base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
    #     speak(" City name ")
    #     print("City name : ")
    #     city_name = takeCommand()
    #     api_key = "Api key"
    #     complete_url = f"{base_url}appid ={api_key}&q ={city_name}"
    #     response = requests.get(complete_url)
    #     x = response.json()

    #     if x["code"] != "404":
    #         y = x["main"]
    #         current_temperature = y["temp"]
    #         current_pressure = y["pressure"]
    #         current_humidiy = y["humidity"]
    #         z = x["weather"]
    #         weather_description = z[0]["description"]
    #         print(
    #             f" Temperature (in kelvin unit) = {str(current_temperature)}"
    #             + "\n atmospheric pressure (in hPa unit) ="
    #             + str(current_pressure)
    #             + "\n humidity (in percentage) = "
    #             + str(current_humidiy)
    #             + "\n description = "
    #             + str(weather_description)
    #         )

    #     else:
    #         speak(" City Not Found ")

    elif "send message " in query:
        # You need to create an account on Twilio to use this service
        account_sid = "Account Sid key"
        auth_token = "Auth token"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=takeCommand(), from_="Sender No", to="Receiver No"
        )

        print(message.sid)

    elif "Good Morning" in query:
        speak(f"A warm{query}")
        speak("How are you Buddy?")
        speak(vaname)

    # most asked question from google Assistant
    elif "will you be my gf" in query or "will you be my bf" in query:
        speak("I'm not sure about, may be you should give me some time")

    elif "i love you" in query:
        speak("It's hard to understand")


if __name__ == "__main__":

    def clear():
        return os.system("cls")

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:
        main(
            add_board=add_board,
            add_card=add_card,
            delete_card=delete_card,
            update_card_name=update_card_name,
            open_card=open_card,
            open_board=open_board,
            add_list=add_list,
            archive_list=archive_list,
            speak=speak,
            takeCommand=takeCommand,
            update_board_name=update_board_name,
            update_list_name=update_list_name,
        )

        # elif "what is" in query or "who is" in query:

        #     # Use the same API key
        #     # that we have generated earlier
        #     client = wolframalpha.Client("API_ID")
        #     res = client.query(query)

        #     try:
        #         print(next(res.results).text)
        #         speak(next(res.results).text)
        #     except StopIteration:
        #         print("No results")

        # elif "" in query:
        # Command go here
        # For adding more commands
