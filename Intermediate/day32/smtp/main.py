import smtplib
import datetime as dt
import random

my_email = "smtplearn01@gmail.com"
my_password = "zxcv@0987"
to_email = "smtplearn01@yahoo.com"

now = dt.datetime.now()
day = now.strftime("%A").title()
with open("quotes.txt") as file:
    quotes_list = file.readlines()

quote_of_the_day = random.choice(quotes_list)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Quote for {day}\n\n{quote_of_the_day}")
