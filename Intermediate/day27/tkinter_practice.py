from tkinter import *

def button_clicked():
    # test = tk_input.get()
    my_label.config(text=tk_input.get())


window = Tk()
# window.config(bg="green")
window.title("BashOps GUI ")
window.minsize(width=800, height=600)
window.config(padx=150, pady=150)

my_label = Label(text="I am a Label", font=("Arial", 18))
my_label["text"] = "Window Label"
# OR
my_label.config(text="Window Label")
# my_label.pack()
# my_label.place(x=150, y=0)
my_label.grid(column=0, row=0)

button = Button(text="Click Here", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="new button")
new_button.grid(column=2, row=0)

tk_input = Entry(window, width=12)
# tk_input.pack()
tk_input.grid(column=3, row=2)
window.mainloop()
