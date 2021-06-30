print("Welcome to the Roller Coaster")

height = int(input("What is your height in CM?  "))
# age = int(input("Enter your age : "))

if height >= 120:
    print("You can ride the Roller Coaster!")
    age = int(input("Enter your age : "))
    if age < 12:
        print("you have to pay : $5")
    elif 12 <= age < 18:  # is equal to "age >= 12 and age < 18:" OR "age < 18:"
        print("you have to pay : $7")
    else:
        print("you have to pay : $12")
else:
    print("Sorry, you have to grow taller before you can ride")