from trello_functions.voiceassistant import speak, takecommand


def add_list(client):
    """
    Add a new list to a Trello board.

    :param client: Trello client object.
    """
    speak("What board do you want to add a list to?")
    board_name = takecommand().lower()
    board = get_board_by_name(client, board_name)
    if board is None:
        speak(f"Board '{board_name}' not found.")
        return
    speak("What do you want to name your list?")
    list_name = takecommand()
    board.add_list(list_name)


def update_list_name(client):
    """
    Update the name of a list on a Trello board.

    :param client: Trello client object.
    """
    speak("What board do you want to update a list from?")
    board_name = takecommand().lower()
    board = get_board_by_name(client, board_name)
    if board is None:
        speak(f"Board '{board_name}' not found.")
        return
    speak("What list do you want to update?")
    list_name = takecommand().lower()
    trello_list = get_list_by_name(board, list_name)
    if trello_list is None:
        speak(f"List '{list_name}' not found on board '{board_name}'.")
        return
    speak("What do you want to update the list name to?")
    new_list_name = takecommand()
    trello_list.set_name(new_list_name)


def archive_list(client):
    """
    Archive a list on a Trello board.

    :param client: Trello client object.
    """
    speak("What board do you want to archive a list from?")
    board_name = takecommand().lower()
    board = get_board_by_name(client, board_name)
    if board is None:
        speak(f"Board '{board_name}' not found.")
        return
    speak("What list do you want to archive?")
    list_name = takecommand().lower()
    trello_list = get_list_by_name(board, list_name)
    if trello_list is None:
        speak(f"List '{list_name}' not found on board '{board_name}'.")
        return
    trello_list.close()
    speak(f"List '{list_name}' archived.")


def get_board_by_name(client, board_name):
    """
    Find a Trello board by name.

    :param client: Trello client object.
    :param board_name: Name of the board to find.
    :return: Trello board object if found, otherwise None.
    """
    for board in client.list_boards():
        if board_name == board.name.lower():
            return board
    return None


def get_list_by_name(board, list_name):
    """
    Find a Trello list by name on a given board.

    :param board: Trello board object.
    :param list_name: Name of the list to find.
    :return: Trello list object if found, otherwise None.
    """
    for trello_list in board.list_lists():
        if list_name == trello_list.name.lower():
            return trello_list
    return None
