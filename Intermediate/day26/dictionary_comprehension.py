# Syntax
# new_dict = {new_key:new_value for item in list}
# OR creating new dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items()}
import random

names = ["Sachin", "Dhoni", "Kohli", "Yuvraj", "Rohit", "Bumrah"]

student_scores = {student: random.randint(30, 100) for student in names}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 50}
print(passed_students)
