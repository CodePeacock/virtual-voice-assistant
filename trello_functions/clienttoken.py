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
)
