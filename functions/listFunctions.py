from functions.voiceAssistant import speak
from functions.voiceAssistant import takeCommand


def add_list(client):
    """
    It takes a Trello client object as an argument, asks the user for the name of a board, and then
    creates a new list on that board with a name that the user provides.

    :param client: the Trello client object
    """
    speak("What board do you want to add a list to?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What do you want to name your list?")
            list_name = takeCommand()
            board.add_list(list_name)


def update_list_name(client):
    """
    This function takes in a Trello client object and asks the user for a board name, then a list name,
    then a new list name. It then updates the list name to the new list name.

    :param client: the Trello client
    """
    speak("What board do you want to update a list from?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to update?")
            list_name = takeCommand().lower()
            lists = board.list_lists()
            for list in lists:
                if list_name in list.name.lower():
                    speak("What do you want to update the list name to?")
                    new_list_name = takeCommand()
                    list.set_name(new_list_name)


def archive_list(client):
    """
    It takes a Trello client object as an argument, asks the user for a board name and a list name, and
    then archives the list.

    :param client: TrelloClient object
    """
    speak("What board do you want to archive a list from?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to archive?")
            list_name = takeCommand().lower()
            lists = board.list_lists()
            for list in lists:
                if list_name in list.name.lower():
                    list.set_closed(True)
