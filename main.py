""" This is the main file of the project. It contains the main function and the switcharray. """
import os

from functions import (
    boardFunctions,
    cardChecklistFunctions,
    cardFunctions,
    clientToken,
    listFunctions,
    voiceAssistant,
)

# vaname = greetUser.VANAME


def using_switcharray():
    """
    This function is the main function of the project. It contains the switcharray.
    """
    # A dictionary.
    switcharray = {
        "add board": boardFunctions.add_board,
        "update board name": boardFunctions.update_board_name,
        "delete board": boardFunctions.close_and_archive_board,
        "add list": listFunctions.add_list,
        "update list name": listFunctions.update_list_name,
        "archive list": listFunctions.archive_list,
        "add card": cardFunctions.add_card,
        "open card": cardFunctions.open_card,
        "update card name": cardFunctions.update_card_name,
        "delete card": cardFunctions.delete_card,
        "add check list": cardChecklistFunctions.add_checklist_item,
        "open trello": boardFunctions.open_trello,
        "exit": exit,
    }

    query = voiceAssistant.takeCommand().lower()

    if query in switcharray:
        switcharray[query](clientToken.CLIENT)
    else:
        voiceAssistant.speak("Sorry, I didn't understand that")


# A way to run the main function only when you want to run the script directly.
if __name__ == "__main__":

    def clear():
        """ This function clears the terminal. """
        return os.system("cls")

    clear()
    # greetUser.wishMe()
    # greetUser.username()

    while True:
        using_switcharray()
