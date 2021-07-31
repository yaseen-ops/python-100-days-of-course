import requests
from datetime import datetime
from blahblah import get_secrets
FILE = "C:/Users/yaseen/secrets/pixela.txt"

USER_NAME = get_secrets(FILE)["USER_NAME"]
API_TOKEN = get_secrets(FILE)["API_TOKEN"]

PIXELA_ENDPOINT = "https://pixe.la/"
USER_ENDPOINT = f"{PIXELA_ENDPOINT}/v1/users"
GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{USER_NAME}/graphs"
GRAPH_ID = "graph1"

user_params = {
    "token": API_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# # Since user created commenting the below line
# response = requests.post(url=USER_ENDPOINT, json=user_params)
# print(response.text)


graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji"
}
header = {
    "X-USER-TOKEN": API_TOKEN
}
# # Since graph got created, now commenting the below line
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=header)
# print(response.text)

# today = datetime.now()
today = datetime(year=2021, month=7, day=16)
# date = f"{today.year}{today.month}{today.day}"
date = today.strftime("%Y%m%d")
graph_update = {
    "date": date,
    "quantity": "9.6"
}
# response = requests.post(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}", json=graph_update, headers=header)
# print(response.text)
new_graph_update = {
    "date": date,
    "quantity": "12.5"
}
# response = requests.put(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{date}", json=new_graph_update, headers=header)
# print(response.text)
response = requests.delete(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{date}", headers=header)
print(response.text)