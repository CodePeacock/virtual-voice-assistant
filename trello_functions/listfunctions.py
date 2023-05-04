"""This file contains functions that deal with lists on Trello boards."""
from trello_functions.voiceassistant import speak, takecommand


def add_list(client):
    """
    It takes a Trello client object as an argument, asks the user for the name of a board, and then
    creates a new list on that board with a name that the user provides.

    :param client: the Trello client object
    """
    speak("What board do you want to add a list to?")
    board_name = takecommand().lower().replace(".", "")
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What do you want to name your list?")
            list_name = takecommand().lower().replace(".","")
            board.add_list(list_name)


def update_list_name(client):
    """Updates the name of a list on a given board"""
    speak("What board do you want to update a list from?")
    board_name = takecommand().lower().replace(".", "")
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to update?")
            list_name = takecommand().lower().replace(".", "")
            lists = board.list_lists()
            for trello_list in lists:
                if list_name in trello_list.name.lower():
                    speak("What do you want to update the list name to?")
                    new_list_name = takecommand()
                    trello_list.set_name(new_list_name)


def archive_list(client):
    """Archives a list from a given board"""
    speak("What board do you want to archive a list from?")
    board_name = takecommand().lower().replace(".", "")
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to archive?")
            list_name = takecommand().lower().replace(".", "")
            lists = board.list_lists()
            for trello_list in lists:
                if list_name in trello_list.name.lower():
                    trello_list.set_closed(True)


def get_board_by_name(client, board_name):
    """
    Find a Trello board by name.

    :param client: Trello client object.
    :param board_name: Name of the board to find.
    :return: Trello board object if found, otherwise None.
    """
    return next(
        (board for board in client.list_boards() if board_name == board.name.lower()),
        None,
    )


def get_list_by_name(board, list_name):
    """
    Find a Trello list by name on a given board.

    :param board: Trello board object.
    :param list_name: Name of the list to find.
    :return: Trello list object if found, otherwise None.
    """
    return next(
        (
            trello_list
            for trello_list in board.list_lists()
            if list_name == trello_list.name.lower()
        ),
        None,
    )
