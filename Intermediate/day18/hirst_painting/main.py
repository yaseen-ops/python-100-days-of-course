import random
import turtle

# import colorgram

# This function just used to extract RGB color codes, which are added in "color_list"
# def extract_colors():
#     colors = colorgram.extract("hirst.jpg", 20)
#     rgb_colors = []
#     for color in colors:
#         # new_color = color.rgb
#         # rgb_colors.append(new_color)
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         new_color = (r, g, b)
#         rgb_colors.append(new_color)
#     print(rgb_colors)


# extract_colors()

color_list = [(201, 164, 112), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44),
              (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32),
              (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48)]

seemaan = turtle.Turtle()
seemaan.shape("turtle")
turtle.colormode(255)
seemaan.speed("fastest")
seemaan.hideturtle()

seemaan.setheading(224)
seemaan.penup()
seemaan.forward(410)
seemaan.setheading(0)

# seemaan.pensize(5)
number_of_dots = 144
for dot_count in range(1, number_of_dots + 1):
    seemaan.dot(20, random.choice(color_list))
    seemaan.forward(50)

    if dot_count % 12 == 0:
        seemaan.setheading(90)
        seemaan.forward(50)
        seemaan.setheading(180)
        seemaan.forward(600)
        seemaan.setheading(0)

my_screen = turtle.Screen()
my_screen.exitonclick()
