from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def get_password():
    website_name = website_entry.get().title()
    email_id = userid_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website_name in data:
        # if website_name in data and email_id in data[website_name]["Email"]:
            # user_email = "".join([value for value in data[website_name]['Email']])
            # user_password = "".join([value for value in data[website_name]['Password']])
            user_email = data[website_name]["Email"]
            user_password = data[website_name]["Password"]
            messagebox.showinfo(title=website_name, message=f"Email ID: {user_email} \nPassword: {user_password}")
        else:
            if not website_name:
                messagebox.showwarning(title="Warning", message="Website is Empty")
            else:
                messagebox.showwarning(title="Warning", message=f"No details for {website_name} exists")


def save_data():
    website_data = website_entry.get().title()
    userid_data = userid_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "Email": userid_data,
            "Password": password_data,
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any field as empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                # data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            userid_entry.delete(0, END)
            userid_entry.insert(0, "dummy@gmail.com")


def on_click(event):
    event.widget.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=75, pady=75)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

userid_label = Label(text="Email/Username:")
userid_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1, row=1)

userid_entry = Entry(width=50)
userid_entry.insert(0, "dummy@gmail.com")
userid_entry.bind("<Button-1>", on_click)  # To clear the default entry on 'click'
userid_entry.grid(column=1, row=2, columnspan=2)

# password_entry = Entry(width=32, show="*")
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

search_password_button = Button(text="Search", width=13, command=get_password)
search_password_button.grid(column=2, row=1)

window.mainloop()
