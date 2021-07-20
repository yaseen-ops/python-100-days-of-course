from turtle import Turtle, Screen

seemaan = Turtle()
seemaan.shape("turtle")
seemaan.turtlesize(0.8)
# seemaan.speed(10)


class DrawShapes:

    def __init__(self, number_of_sides, color):
        self.sides = number_of_sides
        self.pace = 50
        self.color = color

    def draw(self):
        angle = 360 / self.sides
        # seemaan.pencolor(self.color)   # Changes the pen color and the drawing
        seemaan.color(self.color)    # Changes the pen color, the turtle color and the drawing
        for _ in range(self.sides):
            seemaan.forward(self.pace)
            seemaan.right(angle)


    #
    # def get_color(self):
    #     for self.color in pen_color_list:
    #         return self.color


shapes = ["triangle", "square", "pentagon", "hexagon", "heptagon", "octagon", "nonagon", "decagon"]
# If you use the below dictionary
# You can comment line "angle = 3" and "angle += 1" as we are directly getting the angles from dictionary
# if not, comment the dictionary and uncomment the above lines mentioned above
shapes_data = {
        "triangle": 3,
        "square": 4,
        "pentagon": 5,
        "hexagon": 6,
        "heptagon": 7,
        "octagon": 8,
        "nonagon": 9,
        "decagon": 10
    }
pen_color_list = ["red", "black", "green", "grey", "blue", "brown", "purple", "violet"]

seemaan.setheading(120)
seemaan.penup()
seemaan.forward(150)
seemaan.setheading(0)
seemaan.pendown()

# angle = 3

color_list_number = 0
for pick in shapes:
    # seemaan.pencolor(pen_color_list[color_list_number])
    pen_color = pen_color_list[color_list_number]
    # Replace the "DrawShapes(number_of_sides=shapes_data[pick]" to "DrawShapes(number_of_sides=angel",
    # if you are not using the shapes_data dictionary
    shape = DrawShapes(number_of_sides=shapes_data[pick], color=pen_color)
    shape.pace = 75   # Updating the pace from default value in init method
    shape.draw()
    # angle += 1
    color_list_number += 1

seemaan.hideturtle()

my_screen = Screen()
my_screen.exitonclick()
