from data import gk_question_data, history_question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

user_choice = input("Choose the type of question (gk or history?): ").lower()
if user_choice == "gk":
    question_data = gk_question_data
else:
    question_data = history_question_data

for question in question_data:
    question_text = question["question"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.questions_left():
    quiz.next_question()

print("   You've completed the Quiz")
print(f"  Your Final Score is : {quiz.score}/{quiz.question_number}")