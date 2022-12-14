from clientToken import client
from voiceAssistant import speak
from voiceAssistant import takeCommand
import webbrowser


def add_card(client):
    """
    This function will add a card to a list

    :param client: TrelloClient object
    """
    speak("What board do you want to add a card to?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to add a card to?")
            list_name = takeCommand().lower()
            lists = board.list_lists()
            for list in lists:
                if list_name in list.name.lower():
                    speak("What do you want to name your card?")
                    card_name = takeCommand()
                    list.add_card(card_name)


def open_card(client):
    """
    This function will open a card in a list

    :param client: TrelloClient object
    """
    speak("What board do you want to open a card from?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to open a card from?")
            list_name = takeCommand().lower()
            lists = board.list_lists()
            for list in lists:
                if list_name in list.name.lower():
                    speak("What card do you want to open?")
                    card_name = takeCommand().lower()
                    cards = list.list_cards()
                    for card in cards:
                        if card_name in card.name.lower():
                            webbrowser.open(card.url)


def update_card_name(client):
    """
    This function will update a card

    :param client: TrelloClient object
    """
    speak("What board do you want to update a card from?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to update a card from?")
            list_name = takeCommand().lower()
            lists = board.list_lists()
            for list in lists:
                if list_name in list.name.lower():
                    speak("What card do you want to update?")
                    card_name = takeCommand().lower()
                    cards = list.list_cards()
                    for card in cards:
                        if card_name in card.name.lower():
                            speak("What do you want to update the card name to?")
                            new_card_name = takeCommand()
                            card.set_name(new_card_name)


def delete_card(client):
    """
    This function will delete a card

    :param client: TrelloClient object
    """
    speak("What board do you want to delete a card from?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to delete a card from?")
            list_name = takeCommand().lower()
            lists = board.list_lists()
            for list in lists:
                if list_name in list.name.lower():
                    speak("What card do you want to delete?")
                    card_name = takeCommand().lower()
                    cards = list.list_cards()
                    for card in cards:
                        if card_name in card.name.lower():
                            card.delete()
