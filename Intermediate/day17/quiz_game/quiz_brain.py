class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def questions_left(self):
        total_questions = len(self.question_list)
        # if self.question_number < total_questions:
        #     return True
        # else:
        #     return False
        # OR
        return self.question_number < total_questions

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's Wrong!")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("")
