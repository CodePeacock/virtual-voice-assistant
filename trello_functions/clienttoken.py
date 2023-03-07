"""
This file is used to create a client object that will be used to interact with the Trello API.
"""
import os

from dotenv import load_dotenv
from trello import TrelloClient

load_dotenv()

trello_api_key = os.getenv("TRELLO_API_KEY")
trello_token = os.getenv("TRELLO_TOKEN")

# print(trello_api_key, trello_token)

CLIENT = TrelloClient(
    api_key=trello_api_key,
    token=trello_token,
    token_secret="4d54768fba958b54d6e6c5a720aa031e4a66c49ca5223b13ef203daf6486e289",
)
