# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     if index >= len(fruits):
#         raise IndexError(f"Maximum index value is {len(fruits)-1}, but you have given {index}")
#     fruit = fruits[index]
#     print(fruit + " pie")
#
# make_pie(4)


fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + " pie")


make_pie(4)