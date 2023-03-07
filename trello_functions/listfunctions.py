"""This file contains functions that deal with lists on Trello boards."""
from trello_functions.voiceassistant import speak, takecommand


def add_list(client):
    """
    It takes a Trello client object as an argument, asks the user for the name of a board, and then
    creates a new list on that board with a name that the user provides.

    :param client: the Trello client object
    """
    speak("What board do you want to add a list to?")
    board_name = takecommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What do you want to name your list?")
            list_name = takecommand()
            board.add_list(list_name)


def update_list_name(client):
    """Updates the name of a list on a given board"""
    speak("What board do you want to update a list from?")
    board_name = takecommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to update?")
            list_name = takecommand().lower()
            lists = board.list_lists()
            for list in lists:
                if list_name in list.name.lower():
                    speak("What do you want to update the list name to?")
                    new_list_name = takecommand()
                    list.set_name(new_list_name)


def archive_list(client):
    """Archives a list from a given board"""
    speak("What board do you want to archive a list from?")
    board_name = takecommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to archive?")
            list_name = takecommand().lower()
            lists = board.list_lists()
            for list in lists:
                if list_name in list.name.lower():
                    list.set_closed(True)
