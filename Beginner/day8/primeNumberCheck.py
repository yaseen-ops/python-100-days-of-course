#
# def prime_checker(number):
#     for i in range(2, number):
#         if number % i == 0:
#             empty_list.append("0")
#         else:
#             empty_list.append("1")
#
#     if "0" in empty_list:
#         print("It is Not a Prime Number")
#     else:
#         print("It is a Prime Number")


# OR

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It is a Prime Number")
    else:
        print("It is Not a Prime Number")


n = int(input("Check this number: "))
# empty_list = []
prime_checker(number=n)
