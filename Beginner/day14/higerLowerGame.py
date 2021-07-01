import random
from art import logo, vs
from game_data import data

def get_random_account():
    return random.choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description} from {country}"


def compare(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    b_account = get_random_account()

    print(logo)
    continue_game = True
    score = 0

    while continue_game:
        a_account = b_account
        b_account = get_random_account()

        while a_account == b_account:
            b_account = get_random_account()

        print(f"Compare A : {format_data(a_account)}")
        print(vs)
        print(f"Against B : {format_data(b_account)}")
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = a_account["follower_count"]
        b_follower_count = b_account["follower_count"]

        is_correct = compare(user_guess, a_follower_count, b_follower_count)
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
