import os
from trello import TrelloClient
from dotenv import load_dotenv


load_dotenv()

trello_api_key = os.getenv("TRELLO_API_KEY")
trello_token = os.getenv("TRELLO_TOKEN")


# Create a new TrelloClient object
client = TrelloClient(
    api_key=trello_api_key,
    token=trello_token,
    token_secret="4d54768fba958b54d6e6c5a720aa031e4a66c49ca5223b13ef203daf6486e289",
)


def delete_card(client):
    """
    It takes a Trello client as an argument, asks the user for the name of a board, then asks the user
    for the name of a list, then asks the user for the name of a card, then deletes the card.

    :param client: the Trello client object
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


def add_member_board(client):
    """
    It takes a Trello client object as an argument, asks the user for a board name, then asks the user
    for a member name, and then adds the member to the board

    :param client: the Trello client
    """
    speak("What board do you want to add a member to?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What member do you want to add?")
            member_name = takeCommand().lower()
            members = client.list_members()
            for member in members:
                if member_name in member.full_name.title():
                    board.add_member(member)


def move_card(client):
    """
    This function will move a card from one list to another

    :param client: TrelloClient object
    """
    speak("What board do you want to move a card from?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to move a card from?")
            list_name = takeCommand().lower()
            lists = board.list_lists()
            for list in lists:
                if list_name in list.name.lower():
                    speak("What card do you want to move?")
                    card_name = takeCommand().lower()
                    cards = list.list_cards()
                    for card in cards:
                        if card_name in card.name.lower():
                            speak("What list do you want to move the card to?")
                            list_name = takeCommand().lower()
                            lists = board.list_lists()
                            for list in lists:
                                if list_name in list.name.lower():
                                    card.change_list(list.id)


def create_card(client):
    """
    This function will create a card in a list

    :param client: TrelloClient object
    """
    speak("What board do you want to create a card in?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to create a card in?")
            list_name = takeCommand().lower()
            lists = board.list_lists()
            for list in lists:
                if list_name in list.name.lower():
                    speak("What do you want to name the card?")
                    card_name = takeCommand().title()
                    list.add_card(card_name)


def move_list(client):
    """
    This function will move a list from one board to another

    :param client: TrelloClient object
    """
    speak("What board do you want to move a list from?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What list do you want to move?")
            list_name = takeCommand().lower()
            lists = board.list_lists()
            for list in lists:
                if list_name in list.name.lower():
                    speak("What board do you want to move the list to?")
                    board_name = takeCommand().lower()
                    boards = client.list_boards()
                    for board in boards:
                        if board_name in board.name.lower():
                            list.change_board(board.id)


def member_reassign(client):
    """
    This function will reassign a member from one board to another

    :param client: TrelloClient object
    """
    speak("What board do you want to reassign a member from?")
    board_name = takeCommand().lower()
    boards = client.list_boards()
    for board in boards:
        if board_name in board.name.lower():
            speak("What member do you want to reassign?")
            member_name = takeCommand().lower()
            members = client.list_members()
            for member in members:
                if member_name in member.full_name.title():
                    speak("What board do you want to reassign the member to?")
                    board_name = takeCommand().lower()
                    boards = client.list_boards()
                    for board in boards:
                        if board_name in board.name.lower():
                            board.add_member(member)


def add_member_workspaces(client):
    """
    This function will add a member to a workspace

    :param client: TrelloClient object
    """
    speak("What workspace do you want to add a member to?")
    workspace_name = takeCommand().lower()
    workspaces = client.list_organizations()
    for workspace in workspaces:
        if workspace_name in workspace.name.lower():
            speak("What member do you want to add?")
            member_name = takeCommand().lower()
            members = client.list_members()
            for member in members:
                if member_name in member.full_name.title():
                    workspace.add_member(member)


def check_client_guest_workspaces(client):
    """
    This function will check if a member is a guest in a workspace

    :param client: TrelloClient object
    """
    speak("What workspace do you want to check a member in?")
    workspace_name = takeCommand().lower()
    workspaces = client.list_organizations()
    for workspace in workspaces:
        if workspace_name in workspace.name.lower():
            speak("What member do you want to check?")
            member_name = takeCommand().lower()
            members = client.list_members()
            for member in members:
                if member_name in member.full_name.title():
                    if workspace.is_guest(member):
                        speak(f"Yes, {member.full_name} is a guest in {workspace.name}")
                    else:
                        speak(
                            f"No, {member.full_name} is not a guest in {workspace.name}"
                        )


check_client_guest_workspaces(client)
add_member_workspaces(client)
member_reassign(client)
move_list(client)
create_card(client)
move_card(client)
add_member(client)
create_workspace(client)

