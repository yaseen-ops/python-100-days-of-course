import requests
from twilio.rest import Client
import os
from blahblah import get_secrets
FILE = "C:/Users/yaseen/secrets/weather_sms.text"

API_KEY = get_secrets(FILE)["API_KEY"]
MY_LATITUDE = 51.759050
MY_LONGITUDE = 19.458600
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = get_secrets(FILE)["ACCOUNT_SID"]
auth_token = get_secrets(FILE)["AUTH_TOKEN"]
# auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY,
    "exclude": "current,daily,minutely",
}
response = requests.get(WEATHER_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_12_hours = weather_data["hourly"][:12]

will_rain = False
for weather_hourly in weather_12_hours:
    weather_id = weather_hourly["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    # print("Bring an Umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an Umbrella",
            from_='+12243024887',
            to='+919566180254'
        )
    print(message.status)
