import random

print("Welcome to the PyPassword Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in the password? \n"))
nr_symbols = int(input("How many symbols would you like in the password? \n"))
nr_numbers = int(input("How many numbers would you like in the password? \n"))

password_list = []
for char in range(1, nr_letters + 1):
    # random_char = random.choice(letters)
    # password_list.append(random_char)
    # OR
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers):
    password_list.append(random.choice(numbers))

password = ""
for char in password_list:
    password += char

print(password)

# OR

random.shuffle(password_list)    # shuffles the items
password = ""
for char in password_list:
    password += char

print(password)

# OR use without a list, but without list we cannot shuffle the password

password = ""
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char

for char in range(1, nr_symbols + 1):
    random_char = random.choice(symbols)
    password += random_char

for char in range(1, nr_numbers):
    random_char = random.choice(numbers)
    password += random_char

print(password)
