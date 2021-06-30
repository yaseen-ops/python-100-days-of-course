student_scores = input("Enter the list of scores \n").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"Highest score in the class is : {highest_score}")

# OR

highest_score = max(student_scores)
print(f"Highest score in the class is : {highest_score}")