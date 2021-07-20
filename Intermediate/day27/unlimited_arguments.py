def nothing(*args):
    for n in args:
        print(n)


nothing(1, "hello", 4, "hai")


def add(*args):
    print(args[0])
    print(sum(args))


add(1, 4, 6, 7, 8)


# KWARGS = key Word Arguments, which is of type dictionary
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(3, add=3, multiply=5)

