"""
This file contains functions that will add, open, and update cards in a _list
"""
import webbrowser

from trello_functions.voiceassistant import speak, takecommand


def add_card(client):
    """
    This function will add a card to a list.

    :param client: TrelloClient object
    """
    board_name = get_input("What board do you want to add a card to?")
    boards = client.list_boards()
    matching_boards = [board for board in boards if board_name in board.name.lower()]
    if not matching_boards:
        speak(f"Could not find board with name {board_name}")
        return
    board = matching_boards[0]

    list_name = get_input("What list do you want to add a card to?")
    lists = board.list_lists()
    matching_lists = [lst for lst in lists if list_name in lst.name.lower()]
    if not matching_lists:
        speak(f"Could not find list with name {list_name}")
        return
    _list = matching_lists[0]

    card_name = get_input("What do you want to name your card?")
    _list.add_card(card_name)


def get_input(prompt):
    """
    Helper function to get input from user.
    """
    speak(prompt)
    return takecommand().lower().replace(".", "")


def open_card(client):
    """
    This function will open a card in a _list

    :param client: TrelloClient object
    """
    speak("What board do you want to open a card from?")
    board_name = takecommand().lower().replace(".", "")
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What _list do you want to open a card from?")
            list_name = takecommand().lower().replace(".", "")
            lists = board.list_lists()
            for _list in lists:
                if list_name in _list.name.lower():
                    speak("What card do you want to open?")
                    card_name = takecommand().lower().replace(".", "")
                    cards = _list.list_cards()
                    for card in cards:
                        if card_name in card.name.lower():
                            webbrowser.open(card.url)


def update_card_name(client):
    """
    This function will update a card

    :param client: TrelloClient object
    """
    speak("What board do you want to update a card from?")
    board_name = takecommand().lower().replace(".", "")
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What _list do you want to update a card from?")
            list_name = takecommand().lower().replace(".", "")
            lists = board.list_lists()
            for _list in lists:
                if list_name in _list.name.lower():
                    speak("What card do you want to update?")
                    card_name = takecommand().lower().replace(".", "")
                    cards = _list.list_cards()
                    for card in cards:
                        if card_name in card.name.lower():
                            speak("What do you want to update the card name to?")
                            new_card_name = takecommand()
                            card.set_name(new_card_name)


def delete_card(client):
    """
    This function will delete a card

    :param client: TrelloClient object
    """
    speak("What board do you want to delete a card from?")
    board_name = takecommand().lower().replace(".", "")
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What _list do you want to delete a card from?")
            list_name = takecommand().lower().replace(".", "")
            lists = board.list_lists()
            for _list in lists:
                if list_name in _list.name.lower():
                    speak("What card do you want to delete?")
                    card_name = takecommand().lower().replace(".", "")
                    cards = _list.list_cards()
                    for card in cards:
                        if card_name in card.name.lower():
                            card.delete()


def add_label(client):
    """
    This function will add a label to a card

    :param client: TrelloClient object
    """
    speak("What board do you want to add a label to?")
    board_name = takecommand().lower().replace(".", "")
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What _list do you want to add a label to?")
            list_name = takecommand().lower().replace(".", "")
            lists = board.list_lists()
            for _list in lists:
                if list_name in _list.name.lower():
                    speak("What card do you want to add a label to?")
                    card_name = takecommand().lower().replace(".", "")
                    cards = _list.list_cards()
                    for card in cards:
                        if card_name in card.name.lower():
                            speak("What label do you want to add?")
                            label_name = takecommand().lower().replace(".", "")
                            labels = client.list_labels()
                            for label in labels:
                                if label_name in label.name.lower():
                                    card.add_label(label)
