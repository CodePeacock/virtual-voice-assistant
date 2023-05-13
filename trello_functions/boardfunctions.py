"""This module contains functions for interacting with Trello boards"""
import re
import webbrowser

from trello_functions.voiceassistant import speak, takecommand

# board_list = [board.name.lower() for board in client.list_boards()]
# print(board_list)


def get_all_boards(client):
    """
    This function will return a list of all the boards in the user's account

    :param client: TrelloClient object
    :return: list of all the boards in the user's account
    """
    boards = client.list_boards()
    for board in boards:
        print(board.id)


def open_trello(client):
    """
    This function will open the user's trello account

    :param client: TrelloClient object
    """
    webbrowser.open(client.get_member("me").url)


def add_board(client):
    """
    This function will add a board to the user's account

    :param client: TrelloClient object
    """
    speak("What do you want to name your board?")
    board_name = takecommand().lower().replace(".", "")
    board_name = board_name.replace(".", "")
    client.add_board(board_name)


def open_board(client):
    """
    This function will open a board in the user's account

    :param client: TrelloClient object
    """
    speak("What board do you want to open?")
    board_name = takecommand().lower()
    board_name = re.sub(r"[^\w\s]", "", board_name)  # Remove special characters
    board_name = board_name.strip().replace(" ", "-")  # Replace spaces with hyphens
    boards = client.list_boards()
    board_names = {board.name.lower() for board in boards}
    if board_name in board_names:
        matching_board = next(
            board for board in boards if board.name.lower() == board_name
        )
        webbrowser.open(matching_board.url)
    else:
        speak(f"Sorry, I couldn't find a board named {board_name}.")


def update_board_name(client):
    """
    This function will update a board

    :param client: TrelloClient object
    """
    speak("What board do you want to update?")
    board_name = takecommand().lower().replace(".", "")
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What do you want to update the board name to?")
            new_board_name = takecommand().lower().replace(".", "")
            board.set_name(new_board_name)
            speak("Board name updated")


def close_and_archive_board(client):
    """
    This function will close and archive a board

    :param client: TrelloClient object
    """
    speak("What board do you want to close and archive?")
    board_name = takecommand().lower().replace(".", "")
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            board.close()
            board.set_closed(True)
            speak("Board closed and archived")
