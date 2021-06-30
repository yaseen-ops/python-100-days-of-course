alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher(cipher_direction, shift_number, user_text):
    output = ""
    for letter in user_text:
        letter_index = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = letter_index + shift_number
            # Fix for index number out of range
            # or we can copy and paste a-z again in alphabet variable.
            if new_position > 25:
                new_position = new_position - 26
        else:
            new_position = letter_index - shift_number
        new_letter = alphabet[new_position]
        output += new_letter
    print(f"The {cipher_direction}d Text Is {output}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
cipher(cipher_direction=direction, shift_number=shift, user_text=text)