import random

name_input = input("Give everyone's names, separated by Comma. \n")
# Split the input in to individual item and add in to a list
names = name_input.split(", ")

length_of_list = len(names)

# random_choice = random.randint(0, length_of_list - 1)
# pay_person = names[random_choice]
# OR
# pay_person = names[random.randint(0, length_of_list - 1)]
# OR we can use choice function
pay_person = random.choice(names)
print(f"The Person going to pay the bill is {pay_person}")