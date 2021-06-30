import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher(cipher_direction, shift_number, user_text):
    output = ""
    for char in user_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = position + shift_number
                # Fix for index number out of range
                # or we can copy and paste a-z again in alphabet variable.
                if new_position > 25:
                    new_position = new_position - 26
            else:
                new_position = position - shift_number
            new_letter = alphabet[new_position]
            output += new_letter
        else:
            # If in case any space or symbols just add that
            output += char
    print(f"The {cipher_direction}d Text Is {output}")


print(art.logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Fix if the shift value is larger and avoid out of index error
    shift = shift % 26

    cipher(cipher_direction=direction, shift_number=shift, user_text=text)
    choice = input("Type 'Yes' if you want to go again, Otherwise type 'No' \n").lower()
    if choice == "no":
        should_continue = False
        print("Good Bye!")