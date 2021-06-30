import logo
# or
# from logo import treasure_logo
# or
# from logo import *

print(logo.treasure_logo)
# or
# print(treasure_logo)
print("\nWelcome to the treasure island!..")

direction = input("You want to go 'Left' or 'Right' ? \n").lower()

if direction == "left":
    travel = input("You reached Ocean, want to swim? or wait for boat? \n").lower()
    if travel == "wait":
        door = input("Choose a door to knock: 'Red' or 'Yellow' or 'Blue' \n").lower()
        if door == "yellow":
            print("Congratulation!..You found the treasure")
        elif door == "red":
            print("You are burn by fire, Game Over")
        else:
            print("You are been shot, Game Over")
    else:
        print("You are been attached by sea monsters, Game Over")
else:
    print("You fell in to a hole, Game Over")