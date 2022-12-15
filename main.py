import os

# import wolframalpha
import datetime
import webbrowser
import pyjokes


from functions.clientToken import client
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
    """
    It takes a string as input and returns a string as output.

    The input string is the user's voice command.

    The output string is the text that the computer will speak back to the user.

    The function is called with the user's voice command as the input argument.

    The function returns the text that the computer will speak back to the user.

    The text that the computer will speak back to the user is assigned to the variable response.

    The computer speaks the text in the variable response.

    The function is called again with the user's next voice command as the input argument.

    The function returns the text that the computer will speak back to the user.

    The text that the computer will speak back to the user is assigned to the variable response.

    :param client: The Trello client object
    :param open_board: Opens a board
    :param add_board: Add a new board
    :param update_board_name: This function will update the name of the board
    :param add_list: Adds a list to a board
    :param update_list_name: This function will update the name of the list
    :param archive_list: Archives a list
    :param add_card: Adds a card to a list
    :param open_card: Opens a card in the browser
    :param update_card_name: This function will update the name of the card
    :param delete_card: Deletes a card
    :param speak: This is the function that will speak the text that is passed to it
    :param takeCommand: This function takes microphone input from the user and returns string output
    """
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

    elif "search" in query or "play" in query:
        query = query.replace("search", "")
        query = query.replace("play", "")
        webbrowser.open(query)

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
            client=client,
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
