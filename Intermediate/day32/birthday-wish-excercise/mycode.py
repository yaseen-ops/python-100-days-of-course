import smtplib
import datetime as dt
import random
import pandas

PLACEHOLDER = "[NAME]"
my_email = "smtplearn01@gmail.com"
my_password = "zxcv@0987"
service_provider = "smtp.gmail.com"

file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

today = dt.datetime.now().day
month = dt.datetime.now().month

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
for name in data_dict:
    if name["month"] == month and name["day"] == today:
        with open(file_path) as letter:
            letter_data = letter.read()
            person_name = name["name"]
            mail_body = letter_data.replace(PLACEHOLDER, person_name)

        with smtplib.SMTP(service_provider) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=name["email"],
                msg=f"Subject:Happy Birthday!\n\n{mail_body}"
            )
