programming_dictionary = {
    "Cricket": "The Best Cricketer is Sachin",
    "Tennis": "The Best Tennis Player is Djokovic",
    "Football": "The Best Football Player is Christiano Ronaldo"
}

print(programming_dictionary)
# To print a particular Key Value
print(programming_dictionary["Cricket"])

# Creates a new item in the dictionary, if the item already exists then reassign the value
programming_dictionary["Golf"] = "The Best Golfer is Tiger Woods"
programming_dictionary["Cricket"] = "The Best Cricketer is Brain Lara"
print(programming_dictionary)

# Looping in dictionary
for key in programming_dictionary:
    print(key)  # Technically this prints only the key not value
    print(programming_dictionary[key])  # To print the value of the key

