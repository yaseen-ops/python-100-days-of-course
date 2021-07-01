import random
from art import logo

def deal_card():
    """Draws random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Calculate the score of user's and computer's cards"""
    # if 11 in cards and 10 in cards and len(cards) == 0:
    # OR
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has BlackJack!"
    elif user_score == 0:
        return "You won with a BlackJack!"
    elif user_score > 21:
        return "You went over, Lost!"
    elif computer_score > 21:
        return "Opponent went Over, You Won!"
    elif user_score > computer_score:
        return "You Won!"
    else:
        return "You Lose!"


def play_game():
    user_cards = []
    computer_cards = []
    game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User's cards : {user_cards}, current_score : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        print(f"compute score is {computer_score}")

    print(f"  Your final hand : {user_cards} and final score : {user_score}")
    print(f"  Computer's final hand : {computer_cards} and final score : {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to Play a Game of BlackJack, Type 'Y' or 'N': ").lower() == "y":
    print(logo)
    play_game()
