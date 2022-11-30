import requests
import json

id = 'U45LsiBk'

url = "https://api.trello.com/1/boards/5e74a18787c2e22cebf9fbad/lists"

headers = {
    "Accept": "application/json"
}

query = {
    'key': 'db58ee5254120da35e6ae9a3e72029dd',
    'token': '216ba9bd2d7844ad5addfc84b90a796f35a73a3090772e6a57bb8d5d76aad712'
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
)

print(json.dumps(json.loads(response.text),
      sort_keys=True, indent=4, separators=(",", ": ")))
