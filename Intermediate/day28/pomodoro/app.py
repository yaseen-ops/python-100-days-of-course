from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_timer(long_break_secs)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_timer(short_break_secs)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_timer(work_secs)
        timer_label.config(text="Work", fg=GREEN)
    # count_timer(5 * 60)   # = 5 minutes


def count_timer(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # window.after(1000, count_timer, count - 1)
        global timer
        timer = window.after(1000, count_timer, count - 1)
    else:
        start_timer()   # once one timer completes automatically triggers next one
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            check_label.config(text=marks)


def reset_timer():
    window.after_cancel(timer)   # Stop the timer which is defined in function counter_timer
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0   # To reset the reps global variable otherwise it will resume


window = Tk()
window.title("Pomodoro")
window.minsize(width=800, height=600)
window.config(padx=320, pady=200, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# canvas.create_image(100, 112, image="tomato.png") # This doesn't work since it will identify this type of images
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=("Arial", 15), bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=("Arial", 15), bg=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

# check_label = Label(text="✔", font=("Arial", 18), bg=YELLOW, fg=GREEN)
check_label = Label(font=("Arial", 18), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()
