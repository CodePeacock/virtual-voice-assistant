from functions.voiceAssistant import speak
from functions.voiceAssistant import takeCommand
import webbrowser

# board_list = [board.name.lower() for board in client.list_boards()]
# print(board_list)


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


def add_board(client):
    """
    This function will add a board to the user's account

    :param client: TrelloClient object
    """
    speak("What do you want to name your board?")
    board_name = takeCommand()
    client.add_board(board_name)


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
