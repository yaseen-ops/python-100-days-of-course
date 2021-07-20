from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Passing "QuizBrain" gives access to its attributes
        # and makes sure only particular data type is passed
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Time")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=("Arial", 12), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Hello",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_button_image,
                                  highlightthickness=0,
                                  bg=THEME_COLOR,
                                  command=self.true_button_click)
        self.true_button.grid(column=0, row=2)

        self.false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_image,
                                   highlightthickness=0,
                                   bg=THEME_COLOR,
                                   command=self.false_button_click)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Quiz Ended!\nYour Final Score Is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def true_button_click(self):
        # is_right = self.quiz.check_answer("true")
        self.feedback(self.quiz.check_answer("true"))

    def false_button_click(self):
        # is_right = self.quiz.check_answer("false")
        self.feedback(self.quiz.check_answer("false"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
