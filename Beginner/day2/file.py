a = "123"
b = int(a)
print(b+55)

number = input("Enter a two digit number : ")

# input defaults sets the value as string, so have to convert accordingly
print(int(number[0]) + int(number[1]))
# OR
first_digit = number[0]
second_digit = number[1]
result = int(first_digit) + int(second_digit)
print(result)
# print(first_digit + second_digit)