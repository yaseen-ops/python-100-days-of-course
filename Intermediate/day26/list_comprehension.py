odd_numbers = [1, 3, 5, 7]
even_numbers = [item + 1 for item in odd_numbers]
print(odd_numbers)
print(even_numbers)

name = "Dhoni"
name_letters_list = [letter for letter in name]
print(name_letters_list)

range_list = [number * 2 for number in range(1, 5)]
print(range_list)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number * number for number in numbers]
# OR
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)
