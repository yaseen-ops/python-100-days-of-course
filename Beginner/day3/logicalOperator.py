print("Welcome to the Roller Coaster")

height = int(input("What is your height in CM?  "))
# age = int(input("Enter your age : "))

if height >= 120:
    print("You can ride the Roller Coaster!")
    age = int(input("Enter your age : "))
    if age < 12:
        bill = 5
    elif 12 <= age < 18:  # is equal to "age >= 12 and age < 18:" OR "age < 18:"
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        bill = 12

    wants_photo = input("Do you want to take photo? Y or No : ")
    if wants_photo == "Y":
        bill += 3   # Equal to "bill = bill + 3"
    print(f"your total bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride")
