from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# data_frame = pandas.read_csv("data/french_words.csv")
# data_frame_dict = data_frame.to_dict(orient="records")  # separate rows as a separate dictionary in full list
current_card = {}
# try:
#     data_frame = pandas.read_csv("data/words_to_learn.csv")
# except FileNotFoundError:
#     data_frame = pandas.read_csv("data/french_words.csv")
#     data_frame_dict = data_frame.to_dict(orient="records")
# else:
#     data_frame_dict = data_frame.to_dict(orient="records")
### OR ####
try:
    data_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_frame = pandas.read_csv("data/french_words.csv")
data_frame_dict = data_frame.to_dict(orient="records")  # any way we want to convert the csv to dic,
# but to confirm only the CSV file


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_frame_dict)
    card_background.itemconfig(card_title, text="French", fill="black")
    card_background.itemconfig(card_word, text=current_card["French"], fill="black")
    card_background.itemconfig(card_image, image=card_french_image)
    flip_timer = window.after(3000, func=flip_card)  # Timer to flip the card from french to its english meaning


def is_known():
    data_frame_dict.remove(current_card)
    new_data = pandas.DataFrame(data_frame_dict)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    card_background.itemconfig(card_image, image=card_english_image)
    card_background.itemconfig(card_title, text="English", fill="white")
    card_background.itemconfig(card_word, text=current_card["English"], fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)  # Timer to flip the card from french to its english meaning

card_background = Canvas(width=800, height=526)
card_french_image = PhotoImage(file="images/card_front.png")
card_english_image = PhotoImage(file="images/card_back.png")
card_image = card_background.create_image(400, 263, image=card_french_image)
card_background.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = card_background.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = card_background.create_text(400, 263, text="", font=("Arial", 60, "bold"))
card_background.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(column=1, row=1)

next_card()  # calls this function to show the words instead of starting with empty title and word ref: line no. 25 & 26
window.mainloop()
