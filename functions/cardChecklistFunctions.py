"""This file contains functions for adding and removing checklist items from cards"""
from functions.voiceassistant import speak
from functions.voiceassistant import takecommand


def add_checklist_item(client):
    """ This function will add a checklist item to a card"""
    speak("What is the name of the board you want to add a checklist item to?")
    board_name = takecommand()
    speak("What is the name of the list you want to add a checklist item to?")
    list_name = takecommand()
    speak("What is the name of the card you want to add a checklist item to?")
    card_name = takecommand()
    speak("What is the name of the checklist you want to add a checklist item to?")
    checklist_name = takecommand()
    speak("What is the name of the checklist item you want to add?")
    checklist_item_name = takecommand()
    speak("What is the status of the checklist item you want to add?")
    checklist_item_status = takecommand()

    board = client.get_board(board_name)
    list_t = board.get_list(list_name)
    card = list_t.get_card(card_name)
    checklist = card.get_checklist(checklist_name)
    checklist.add_checklist_item(checklist_item_name, checklist_item_status)

    speak("Checklist item added")
