import random
import logo

rock = logo.rock
paper = logo.paper
scissors = logo.scissors
game_logo = [rock, paper, scissors]


user_choice = int(input("What do you choose? Type 0 for Rock, 1 or Paper or 2 for Scissors \n"))
if user_choice >= 3 or user_choice < 0:
    print("You enter an invalid option, You Lose!")
else:
    print("   You Chose !")
    print(game_logo[user_choice])
    print("   Computer Chose !")
    computer_choice = random.randint(0, 2)
    print(game_logo[computer_choice])

    if user_choice == 0 and computer_choice == 1:
        print("Sorry, You Lose!")
    elif user_choice == 1 and computer_choice == 2:
        print("Sorry, You Lose!")
    elif user_choice == 2 and computer_choice == 0:
        print("Sorry, You Lose!")
    elif user_choice == computer_choice:
        print("Match Drawn!")
    else:
        print("Congratulation! You Won!")
