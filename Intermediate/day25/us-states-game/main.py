import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's the state name?").title()
    if answer_state == "Exit":
        # Create CSV with data of missed states in QUIZ
        missed_states = [state for state in all_states if state not in guessed_states]
        # Replaced the below lines with list conditional list comprehension as above
        # missed_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        df = pandas.DataFrame(missed_states)
        df.to_csv("missed_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        turtle_state = turtle.Turtle()
        turtle_state.hideturtle()
        turtle_state.penup()
        state_data = data[data.state == answer_state]
        turtle_state.goto(int(state_data.x), int(state_data.y))
        # turtle_state.write(answer_state)
        # OR
        turtle_state.write(state_data.state.item())  # added .item() to only print state name without index, object


# screen.exitonclick()
