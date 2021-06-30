import replit
import random
from art import logo,stages
import hangman_words

# word_list = ["Chennai", "Mumbai", "Madurai", "Kolkata", "Bangalore", "Hyderabad"]
word_list = hangman_words.word_list
chosen_word = random.choice(word_list).lower()

word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display.append("_")
print(logo)

lives = 6
is_game_over = False
while not is_game_over:
    guess = input("Guess a Letter : ").lower()
    replit.clear()
    if guess in display:
        print("You are already guess the letter "+guess)
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"you guessed {guess}, that's not in the word, You lose a life")
        lives -= 1
        if lives == 0:
            is_game_over = True
            print("You Lose! Game Over!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        is_game_over = True
        print("You Won! Game Over!")
    print(display)

    print(f"Number of lives left : {lives}")
    print(stages[lives])