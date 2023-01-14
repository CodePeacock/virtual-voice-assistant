from functions import (
    clientToken,
    cardChecklistFunctions,
    cardFunctions,
    boardFunctions,
    listFunctions,
)


class trello_Array:
    def __init__(self, client):
        self.client = clientToken.CLIENT
        self.switch = {
            "open board": self.open_board,
            "add board": self.add_board,
            "update board name": self.update_board_name,
            "delete board": self.close_and_archive_board,
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
        boardFunctions.open_board(self.client)

    def add_board(self):
        boardFunctions.add_board(self.client)

    def update_board_name(self):
        boardFunctions.update_board_name(self.client)

    def delete_board(self):
        boardFunctions.delete_board(self.client)

    def add_list(self):
        listFunctions.add_list(self.client)

    def update_list_name(self):
        listFunctions.update_list_name(self.client)

    def archive_list(self):
        listFunctions.archive_list(self.client)

    def add_card(self):
        cardFunctions.add_card(self.client)

    def open_card(self):
        cardFunctions.open_card(self.client)

    def update_card_name(self):
        cardFunctions.update_card_name(self.client)

    def delete_card(self):
        cardFunctions.delete_card(self.client)

    def add_checklist(self):
        cardChecklistFunctions.add_checklist(self.client)

    def exit(self):
        exit()

    def run(self, query):
        self.switch.get(query, lambda: print("Invalid"))()
