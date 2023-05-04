"""
This is the main file for the Trello Voice Assistant.
"""

import os

from trello_functions import clienttoken, trello_array, voiceassistant


def run_voice_command():
    """Run the main voice command loop."""
    switchmap = trello_array(clienttoken.CLIENT)
    switch_map = {
        "create board": switchmap.add_board,
        "update board name": switchmap.update_board_name,
        # "delete board": trello_array.close_and_archive_board,
        "add list": switchmap.add_list,
        "update list name": switchmap.update_list_name,
        "archive list": switchmap.archive_list,
        "add card": switchmap.add_card,
        "open card": switchmap.open_card,
        "update card name": switchmap.update_card_name,
        "delete card": switchmap.delete_card,
        "open trello": switchmap.open_trello,
        "open board": switchmap.open_board,
        "exit": switchmap.exit,
    }

    try:
        command = voiceassistant.takecommand().lower().replace(".", "")
        query: str = command
        print(f"You said: {query}")

        if query in switch_map:
            switch_map[query]()
        else:
            voiceassistant.speak("Sorry, I didn't understand that")
    except Exception as error:
        print(error)
        raise


if __name__ == "__main__":

    def clear_terminal():
        """Clear the terminal."""
        return os.system("cls")

    clear_terminal()

    while True:
        run_voice_command()
