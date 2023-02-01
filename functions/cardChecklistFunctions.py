from functions.voiceAssistant import speak
from functions.voiceAssistant import takeCommand


def add_checklist_item(client):
    speak("What is the name of the board you want to add a checklist item to?")
    board_name = takeCommand()
    speak("What is the name of the list you want to add a checklist item to?")
    list_name = takeCommand()
    speak("What is the name of the card you want to add a checklist item to?")
    card_name = takeCommand()
    speak("What is the name of the checklist you want to add a checklist item to?")
    checklist_name = takeCommand()
    speak("What is the name of the checklist item you want to add?")
    checklist_item_name = takeCommand()
    speak("What is the status of the checklist item you want to add?")
    checklist_item_status = takeCommand()

    board = client.get_board(board_name)
    list_t = board.get_list(list_name)
    card = list_t.get_card(card_name)
    checklist = card.get_checklist(checklist_name)
    checklist.add_checklist_item(checklist_item_name, checklist_item_status)

    speak("Checklist item added")
