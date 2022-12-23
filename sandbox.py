from pprint import pprint
from functions import clientToken

board_id = "5ce76d7e47a76361ee6f58e9"


def get_trello_board(board_id):
    import requests

    url = f"https://api.trello.com/1/boards/{board_id}"
    querystring = {
        "key": "db58ee5254120da35e6ae9a3e72029dd",
        "token": "216ba9bd2d7844ad5addfc84b90a796f35a73a3090772e6a57bb8d5d76aad712",
    }
    response = requests.request("GET", url, params=querystring)
    return response.json()


pprint(get_trello_board(board_id))


def get_all_boards(client):
    """
    This function will return a list of all the boards in the user's account

    :param client: TrelloClient object
    """
    boards = client.list_boards()
    for board in boards:
        # print(board.name)
        print(board.id)


# get_all_boards(clientToken.client)
