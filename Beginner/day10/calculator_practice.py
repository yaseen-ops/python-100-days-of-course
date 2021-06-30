
def add(n1, n2):
    """ Addition of two numbers """
    return n1 + n2


def sub(n1, n2):
    """ Subtraction of two numbers """
    return n1 - n2


def multiply(n1, n2):
    """ Multiplication of two numbers """
    return n1 * n2


def divide(n1, n2):
    """ Division of two numbers """
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}

# Changed 'int' to 'float' to do calculation for floating numbers as well
num1 = float(input("Enter the first number : "))
for operator_symbol in operations:
    print(operator_symbol)
operator = input("Pick an operation from the line above : ")
num2 = float(input("Enter the second number : "))

calculation_fun = operations[operator]
answer = round(calculation_fun(num1, num2), 2)
print(f"{num1} {operator} {num2} = {answer}")