import requests
from datetime import datetime
import smtplib
from blahblah import get_secrets
FILE = "C:/Users/yaseen/secrets/mail.txt"

MY_LATITUDE = 8.669624
MY_LONGITUDE = 77.589635
MY_EMAIL = get_secrets(FILE)["EMAIL_ID"]
MY_PASSWORD = get_secrets(FILE)["EMAIL_PASSWORD"]

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_data = iss_response.json()
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5:
        return True


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0]
    # sunset = data["results"]["sunset"].split("T")[1].split("+")[0]
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


# hour = datetime.now().hour
# minute = datetime.now().minute
# current_time = f"{hour}:{minute}"
# print(f"Current time: {current_time}")
# print(f"Sunrise: {sunrise}")
# print(f"Sunset: {sunset}")

if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Look Up\n\nThe ISS is above you in the sky."
        )
