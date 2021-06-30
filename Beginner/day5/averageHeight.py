student_heights = input("Enter the bunch of heights: \n").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)

total_height = 0
total_students = 0
for student_height in student_heights:
    total_students += 1
    total_height += student_height

average_height = round(total_height / total_students)
print(average_height)

# OR

total_height = sum(student_heights)
total_students = len(student_heights)
average_height = round(total_height / total_students)
print(average_height)