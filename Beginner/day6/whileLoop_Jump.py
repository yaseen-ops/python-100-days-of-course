def turn_left():
    print("Nothing")


def move():
    print("Nothing")


def front_is_clear():
    print("Nothing")


def wall_in_front():
    print("Nothing")


def wall_on_right():
    print("Nothing")

def at_goal():
    print("Nothing")


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()

    turn_right()
    move()
    turn_right()

    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()