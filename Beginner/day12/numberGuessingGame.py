import random
from art import logo

EASY_LEVEL_TURNS = 10
MEDIUM_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'medium' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "medium":
        return MEDIUM_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def number_check(user_guess, answer, turns):
    if user_guess < 1 or user_guess > 100:
        return turns - turns
    elif user_guess > answer:
        print("It's high")
        return turns - 1
    elif user_guess < answer:
        print("It's low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        turns = number_check(guess, answer, turns)
        if turns == 0:
            game_over = True
            print("You ran out of turns, You Lose!")
            return
        elif guess != answer:
            print("Guess again")


game()
