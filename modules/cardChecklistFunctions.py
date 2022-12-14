from clientToken import client
from voiceAssistant import speak
from voiceAssistant import takeCommand


def add_checklist(client):
    """
    This function will add a checklist to a card

    :param client: TrelloClient object
    """
    speak("What board do you want to add a checklist to?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to add a checklist to?")
            list_name = takeCommand().lower()
            lists = board.list_lists()
            for list in lists:
                if list_name in list.name.lower():
                    speak("What card do you want to add a checklist to?")
                    card_name = takeCommand().lower()
                    cards = list.list_cards()
                    for card in cards:
                        if card_name in card.name.lower():
                            speak("What do you want to name your checklist?")
                            checklist_name = takeCommand()
                            card.add_checklist(checklist_name)
