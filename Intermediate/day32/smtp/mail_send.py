import smtplib

my_email = "smtplearn01@gmail.com"
my_password = "zxcv@0987"
to_email = "smtplearn01@yahoo.com"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="Subject:Hello\n\nBody of the mail")
# connection.close()

# OR
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="Subject:Hello\n\nBody of the mail")

