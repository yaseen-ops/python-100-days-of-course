import smtplib
from datetime import datetime
import random
import pandas

PLACEHOLDER = "[NAME]"
my_email = "smtplearn01@gmail.com"
my_password = "zxcv@0987"
service_provider = "smtp.gmail.com"

today = (datetime.now().month, datetime.now().day)

letters_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
letter = random.choice(letters_list)


data = pandas.read_csv("birthdays.csv")
data_dict = {(row_data.month, row_data.day): row_data for (index, row_data) in data.iterrows()}

if today in data_dict:
    birthday_person = data_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        letter_content = contents.replace(PLACEHOLDER, birthday_person["name"])
        print(letter_content)

    with smtplib.SMTP(service_provider) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter_content}"
        )


