"""This file contains the switch array class which is used to call the functions"""
from functions import (
    boardfunctions,
    cardChecklistFunctions,
    cardfunctions,
    clienttoken,
    listfunctions,
)


class trello_Array:
    """This class contains the switch array which is used to call the functions"""
    def __init__(self, client):
        self.client = clienttoken.CLIENT
        self.switch = {
            "open board": self.open_board,
            "add board": self.add_board,
            "update board name": self.update_board_name,
            "add list": self.add_list,
            "update list name": self.update_list_name,
            "archive list": self.archive_list,
            "add card": self.add_card,
            "open card": self.open_card,
            "update card name": self.update_card_name,
            "delete card": self.delete_card,
            "exit": self.exit,
        }

    def open_board(self):
        boardfunctions.open_board(self.client)

    def add_board(self):
        boardfunctions.add_board(self.client)

    def update_board_name(self):
        boardfunctions.update_board_name(self.client)

    def delete_board(self):
        boardfunctions.delete_board(self.client)

    def add_list(self):
        listfunctions.add_list(self.client)

    def update_list_name(self):
        listfunctions.update_list_name(self.client)

    def archive_list(self):
        listfunctions.archive_list(self.client)

    def add_card(self):
        cardfunctions.add_card(self.client)

    def open_card(self):
        cardfunctions.open_card(self.client)

    def update_card_name(self):
        cardfunctions.update_card_name(self.client)

    def delete_card(self):
        cardfunctions.delete_card(self.client)

    def add_checklist(self):
        cardChecklistFunctions.add_checklist(self.client)

    def exit(self):
        exit()

    def run(self, query):
        self.switch.get(query, lambda: print("Invalid"))()
