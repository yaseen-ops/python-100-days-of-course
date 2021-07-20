import requests

API_KEY = "720f773533fdf5fe413ca07eae748e5c"
MY_LATITUDE = 8.669624
MY_LONGITUDE = 77.589635
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY,
    "exclude": "current,daily,minutely",
}

# response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Chennai&appid={API_KEY}") print(
# response.json()) response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LATITUDE}&lon={
# MY_LONGITUDE}&exclude=hourly,daily&appid={API_KEY}")
response = requests.get(WEATHER_ENDPOINT, params=parameters)
# print(response.status_code)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])

weather_12_hours = [weather_hourly["weather"][0]["id"] for weather_hourly in weather_data["hourly"]]
will_rain = False
for weather in weather_12_hours[:12]:
    if weather < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")