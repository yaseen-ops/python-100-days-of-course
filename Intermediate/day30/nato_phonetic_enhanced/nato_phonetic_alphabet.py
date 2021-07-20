import pandas


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_list = [nato_phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, Only letters in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic_list)


nato = pandas.read_csv("../../day26/nato_phonetic_alphabet.csv")
nato_phonetic_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

generate_phonetic()
