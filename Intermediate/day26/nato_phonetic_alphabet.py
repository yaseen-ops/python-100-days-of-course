import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
# print(nato_phonetic_dict)

user_input = input("Enter a word: ").upper()
# phonetic_list = []
# for letter in user_input:
#     phonetic_list.append(nato_phonetic_dict[letter])
#
# print(phonetic_list)
phonetic_list = [nato_phonetic_dict[letter] for letter in user_input]
print(phonetic_list)
