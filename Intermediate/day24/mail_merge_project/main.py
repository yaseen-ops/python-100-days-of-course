PLACEHOLDER = "[name]"
# Create a list from reading data from a file
with open("Input/Names/invited_names.txt") as file:
    name_list = file.readlines()

# # Read data from file and save in mail_data
# with open("Input/Letters/starting_letter.txt") as letter:
#     mail_data = letter.read()
#
# # Create mail letters
# for person in name_list:
#     person_name = person.strip()   # removing "spaces" @ beginning/end
#     mail_letter = f"Output/ReadyToSend/{person_name}.txt"  # set the mail letter name
#     with open(mail_letter, mode="w") as write_mail:    # opening/creating mail letter as write mode
#         # writing the data in mail letter and replacing the dummy name with person's name
#         write_mail.write(mail_data.replace(PLACEHOLDER, f"{person_name}"))

# OR as below

with open("Input/Letters/starting_letter.txt") as letter:
    mail_data = letter.read()
    for name in name_list:
        new_name = name.strip()
        new_mail_data = mail_data.replace(PLACEHOLDER, new_name)
        mail_letter = f"Output/ReadyToSend/letter_for_{new_name}.txt"
        with open(mail_letter, mode="w") as write_mail:
            write_mail.write(new_mail_data)
