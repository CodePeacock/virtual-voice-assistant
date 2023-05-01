"""
Create a client object to interact with the Trello API.
"""

import os
from typing import Optional, cast

from dotenv import load_dotenv
from trello import TrelloClient

load_dotenv()

trello_api_key = cast(Optional[str], os.getenv("TRELLO_API_KEY"))
trello_token = cast(Optional[str], os.getenv("TRELLO_TOKEN"))

if trello_api_key is None or trello_token is None:
    raise ValueError("Trello API key and token are required.")

CLIENT: TrelloClient = TrelloClient(
    api_key=trello_api_key,
    token=trello_token,
)
