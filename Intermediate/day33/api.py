import requests


response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)

# response = requests.get(url="http://api.open-notify.org/issow.json")
# print(response.status_code)
# response.raise_for_status()

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)
