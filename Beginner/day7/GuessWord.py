import random
import art

word_list = ["Chennai", "Madurai", "Singapore", "England"]

chosen_word = random.choice(word_list).lower()

word_length = len(chosen_word)
display = []
for letter in range(word_length):
    display.append("_")


def game():
    guess = input("Guess a Letter : ").lower()

    # number = 0
    # for letter in chosen_word:
    #     if guess == letter:
    #         display[number] = letter
    #
    #     number += 1
    # OR
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)


is_game_over = False

# Check all the letters are filled with unlimited tries
while not is_game_over:
    game()
    if "_" not in display:
        is_game_over = True
        print("Game Over!")