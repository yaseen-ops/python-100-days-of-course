alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(shift_number, plain_text):
    cipher_text = ""
    for letter in plain_text:
        letter_index = alphabet.index(letter)
        new_position = letter_index + shift_number
        # Fix for index number out of range
        # or we can copy and paste a-z again in alphabet variable.
        if new_position > 25:
            new_position = new_position - 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The Encoded Text Is {cipher_text}")


def decrypt(shift_number, cipher_text):
    plain_text = ""
    for letter in cipher_text:
        letter_index = alphabet.index(letter)
        new_position = letter_index - shift_number
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The Decoded Text Is {plain_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == "encode":
    encrypt(shift_number=shift, plain_text=text)
elif direction == "decode":
    decrypt(shift_number=shift, cipher_text=text)
else:
    print("Please Type only 'encode' or 'decode' ")