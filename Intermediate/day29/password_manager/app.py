from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    # Copying the password to clipboard
    # password_entry.clipboard_clear()
    # password_entry.clipboard_append(password)
    # OR use the pyperclip module to copy to clipboard to take of above two steps in one line
    pyperclip.copy(password)


def save_data():
    website_data = website_entry.get()
    userid_data = userid_entry.get()
    password_data = password_entry.get()

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any filed as empty")
    else:
        is_ok = messagebox.askokcancel(title=website_data,
                                       message=f"These are the details entered: \nEmail: {userid_data} "
                                               f"\nPassword: {password_data} \nIs it Ok to Save?")
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website_data} | {userid_data} | {password_data}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            userid_entry.delete(0, END)
            userid_entry.insert(0, "dummy@gmail.com")


def on_click(event):
    event.widget.delete(0, END)


window = Tk()
window.title("Password Manager")
# window.minsize(width=800, height=600)
window.config(padx=75, pady=75)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
# website_label.config(padx=5, pady=5)
website_label.grid(column=0, row=1)

userid_label = Label(text="Email/Username:")
# userid_label.config(padx=5, pady=5)
userid_label.grid(column=0, row=2)

password_label = Label(text="Password:")
# password_label.config(padx=5, pady=5)
password_label.grid(column=0, row=3)

website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

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

window.mainloop()
