from tkinter import *


# def miles_to_km():
#     km_result.delete(0, "end")
#     miles = float(miles_input.get())
#     km = round(miles * 1.609344, 1)
#     km_result.insert(0, str(km))
def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609344, 1)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles To Kilometers Conversion")
window.minsize(width=800, height=600)
window.config(padx=250, pady=200)

is_equal_label = Label(text="is equal to", font=("Arial", 14))
is_equal_label.grid(column=0, row=1)

miles_input = Entry(window, width=12)
miles_input.grid(column=1, row=0)

# km_result = Entry(window, width=12)
# km_result.grid(column=1, row=1)

miles_label = Label(text="Miles", font=("Arial", 14))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 14))
km_label.grid(column=2, row=1)

km_result_label = Label(text="0", font=("Arial", 14))
km_result_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", font=("Arial", 15), command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()