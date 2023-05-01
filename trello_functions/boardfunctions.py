"""This module contains functions for interacting with Trello boards"""
import webbrowser
from trello_functions.voiceassistant import speak, takecommand


def get_all_boards(client):
    """
    Returns a list of all the boards in the user's account.

    :param client: TrelloClient object
    :return: List of board IDs
    """
    return [board.id for board in client.list_boards()]


def open_trello(client):
    """
    Opens the user's Trello account in a web browser.

    :param client: TrelloClient object
    """
    webbrowser.open(client.get_member("me").url)


def add_board(client):
    """
    Adds a board to the user's account.

    :param client: TrelloClient object
    """
    speak("What do you want to name your board?")
    board_name = takecommand().lower().replace(" ", ".")
    try:
        client.add_board(board_name)
        speak(f"Board '{board_name}' added.")
    except Exception as e:
        speak(f"Error adding board: {str(e)}")


def open_board(client):
    """
    Opens a board in the user's account.

    :param client: TrelloClient object
    """
    speak("What board do you want to open?")
    board_name = takecommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            webbrowser.open(board.url)
            return
    speak(f"Board '{board_name}' not found.")


def update_board_name(client):
    """
    Updates the name of a board.

    :param client: TrelloClient object
    """
    speak("What board do you want to update?")
    board_name = takecommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What do you want to update the board name to?")
            new_board_name = takecommand()
            try:
                board.set_name(new_board_name)
                speak("Board name updated.")
            except Exception as e:
                speak(f"Error updating board name: {str(e)}")
            return
    speak(f"Board '{board_name}' not found.")


def close_and_archive_board(client):
    """
    Closes and archives a board.

    :param client: TrelloClient object
    """
    speak("What board do you want to close and archive?")
    board_name = takecommand().lower()
    boards = client.list_
