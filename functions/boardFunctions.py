import webbrowser
from logging import Logger as logger

from functions.voiceAssistant import speak, takeCommand

# board_list = [board.name.lower() for board in client.list_boards()]
# print(board_list)


def get_all_boards(client):
    """
    This function will return a list of all the boards in the user's account

    :param client: TrelloClient object
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
    board_name = takeCommand()
    client.add_board(board_name)


def open_board(client):
    """
    This function will open a board in the user's account

    :param client: TrelloClient object
    """
    speak("What board do you want to open?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            webbrowser.open(board.url)


def update_board_name(client):
    """
    This function will update a board

    :param client: TrelloClient object
    """
    speak("What board do you want to update?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What do you want to update the board name to?")
            new_board_name = takeCommand()
            board.set_name(new_board_name)
            speak("Board name updated")
            logger.info(f"Board name updated to {new_board_name}")


def close_and_archive_board(client):
    """
    This function will close and archive a board

    :param client: TrelloClient object
    """
    speak("What board do you want to close and archive?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            board.close()
            board.set_closed(True)
            speak("Board closed and archived")
