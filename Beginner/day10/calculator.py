# from replit import clear
import art

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


def list_operators():
    """ It lists all the available operators for calculation """
    for operator_symbol in operations:
        print(operator_symbol)


operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}


def calculator():
    """ function calculates the given two values """
    print(art.logo)
    # Changed 'int' to 'float' to do calculation for floating numbers as well
    num1 = float(input("Enter the first number : "))
    end_calculation = False

    while not end_calculation:
        list_operators()
        operator = input("Pick an operation : ")
        num2 = float(input("Enter the next number : "))
        calculation_fun = operations[operator]
        answer = round(calculation_fun(num1, num2), 2)
        print(f"{num1} {operator} {num2} = {answer}")

        wish_to_continue = input("Type 'Y' to Continue or Type 'N' to Exit : ").lower()
        if wish_to_continue == "y":
            num1 = answer
        else:
            # clear()
            end_calculation = True
            # recursive function call to restart the calculation freshly when user doesn't want to continue
            calculator()


calculator()
