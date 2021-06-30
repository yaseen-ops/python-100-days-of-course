import math


def paint_calc(height, width, cover):
    area = test_h * test_w
    number_of_cans = math.ceil(area / coverage)
    print(f"You'll need {number_of_cans} cans of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)