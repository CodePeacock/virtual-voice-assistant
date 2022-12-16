import os


from functions import (
    clientToken,
    cardChecklistFunctions,
    cardFunctions,
    boardFunctions,
    listFunctions,
    voiceAssistant,
    greetUser,
)

vaname = greetUser.VANAME


def using_switchArray():
    """
    It takes a command from the user, and if the command is in the switchArray, it executes the function
    associated with that command
    """
    switchArray = {
        "open trello": boardFunctions.open_board,
        "add board": boardFunctions.add_board,
        "update board name": boardFunctions.update_board_name,
        "add list": listFunctions.add_list,
        "update list name": listFunctions.update_list_name,
        "archive list": listFunctions.archive_list,
        "add card": cardFunctions.add_card,
        "open card": cardFunctions.open_card,
        "update card name": cardFunctions.update_card_name,
        "delete card": cardFunctions.delete_card,
        "add checklist": cardChecklistFunctions.add_checklist,
    }

    query = voiceAssistant.takeCommand().lower()

    if query in switchArray:
        switchArray[query](clientToken.client)
    else:
        voiceAssistant.speak("Sorry, I didn't understand that")


# def main(
#     client,
#     speak,
#     takeCommand,
#     open_board,
#     add_board,
#     update_board_name,
#     add_list,
#     update_list_name,
#     archive_list,
#     add_card,
#     open_card,
#     update_card_name,
#     delete_card,
#     add_checklist,
# ):
#     """
#     It takes a string as input and returns a string as output.

#     The input string is the user's voice command.

#     The output string is the text that the computer will speak back to the user.

#     The function is called with the user's voice command as the input argument.

#     The function returns the text that the computer will speak back to the user.

#     The text that the computer will speak back to the user is assigned to the variable response.

#     The computer speaks the text in the variable response.

#     The function is called again with the user's next voice command as the input argument.

#     The function returns the text that the computer will speak back to the user.

#     The text that the computer will speak back to the user is assigned to the variable response.

#     :param client: The Trello client object
#     :param open_board: Opens a board
#     :param add_board: Add a new board
#     :param update_board_name: This function will update the name of the board
#     :param add_list: Adds a list to a board
#     :param update_list_name: This function will update the name of the list
#     :param archive_list: Archives a list
#     :param add_card: Adds a card to a list
#     :param open_card: Opens a card in the browser
#     :param update_card_name: This function will update the name of the card
#     :param delete_card: Deletes a card
#     :param speak: This is the function that will speak the text that is passed to it
#     :param takeCommand: This function takes microphone input from the user and returns string output
#     """
#     query = takeCommand().lower()

#     if "open trello" in query:
#         webbrowser.open("https://trello.com/")

#     elif "open board" in query:
#         open_board(client)

#     elif "add board" in query:
#         add_board(client)

#     elif "update board name" in query:
#         update_board_name(client)

#     elif "add list" in query:
#         add_list(client)

#     elif "update list name" in query:
#         update_list_name(client)

#     elif "archive list" in query:
#         archive_list(client)

#     elif "add card" in query:
#         add_card(client)

#     elif "open card" in query:
#         open_card(client)

#     elif "update card name" in query:
#         update_card_name(client)

#     elif "delete card" in query:
#         delete_card(client)

#     elif "the time" in query:
#         strTime = datetime.datetime.now().strftime("% H:% M:% S")
#         speak(f"Sir, the time is {strTime}")

#     elif "how are you" in query:
#         speak("I am fine, Thank you")
#         speak("How are you, Sir")

#     elif "fine" in query or "good" in query:
#         speak("It's good to know that your fine")

#     elif "change my name to" in query:
#         query = query.replace("change my name to", "")
#         vaname = query

#     elif "change name" in query:
#         speak("What would you like to call me, Sir ")
#         vaname = takeCommand()
#         speak("Thanks for naming me")

#     elif "exit" in query:
#         speak("Thanks for giving me your time")
#         exit()

#     elif "joke" in query:
#         speak(pyjokes.get_joke())
#         print(pyjokes.get_joke())

#     elif "search" in query or "play" in query:
#         query = query.replace("search", "")
#         query = query.replace("play", "")
#         webbrowser.open(query)


if __name__ == "__main__":

    def clear():
        return os.system("cls")

    # This Function will clean any
    # command before execution of this python file
    clear()
    greetUser.wishMe()
    greetUser.username()
    using_switchArray()
    # while True:
    #     main(
    #         client=clientToken.client,
    #         speak=voiceAssistant.speak,
    #         takeCommand=voiceAssistant.takeCommand,
    #         add_board=boardFunctions.add_board,
    #         open_board=boardFunctions.open_board,
    #         update_board_name=boardFunctions.update_board_name,
    #         add_card=cardFunctions.add_card,
    #         open_card=cardFunctions.open_card,
    #         update_card_name=cardFunctions.update_card_name,
    #         delete_card=cardFunctions.delete_card,
    #         add_list=listFunctions.add_list,
    #         archive_list=listFunctions.archive_list,
    #         update_list_name=listFunctions.update_list_name,
    #         add_checklist=cardChecklistFunctions.add_checklist,
    #     )
