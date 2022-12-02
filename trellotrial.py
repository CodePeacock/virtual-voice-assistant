from trello import TrelloClient


client = TrelloClient(
    api_key="db58ee5254120da35e6ae9a3e72029dd",
    token="216ba9bd2d7844ad5addfc84b90a796f35a73a3090772e6a57bb8d5d76aad712",
    token_secret="4d54768fba958b54d6e6c5a720aa031e4a66c49ca5223b13ef203daf6486e289",
)

boards = client.list_boards()

for board in boards:
    print(board.name)
    print(board.id)
    print(board.url)

single_board = client.get_board("5e74a18787c2e22cebf9fbad")
# lists = single_board.all_lists()
# for list_ in lists:
#     print(list_.name)
#     print(list_.id)

# 5e75cb99a77dcc6db71cf5f4

cards = single_board.get_cards()
# Card name, description, ID, URL
cards
for card in cards:
    # print(card.name)
    # print(card.desc)
    # print(card.id)
    # print(card.url)
    if card.name == "Python Test Card":
        print(card.id)
