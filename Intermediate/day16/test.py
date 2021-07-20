def fact(number):
    if number == 1:
        return 1
    return fact(number-1)*number


print(fact(4))