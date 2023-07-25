# Importing turtle library to draw python logo
import turtle

# Creating our turtle cursor to draw
my_turtle_cursor = turtle.Turtle()

# Creating a separate Canvas to draw Python Logo
my_turtle_screen = turtle.Screen()

#  Creating a pause function to pause the cursor
def pause():
    my_turtle_cursor.speed(2)
    for i in range(100):
        my_turtle_cursor.left(90)



def draw_upper_dot_of_python_logo():
    my_turtle_cursor.penup()
    my_turtle_cursor.right(90)
    my_turtle_cursor.forward(160)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(70)
    my_turtle_cursor.pencolor("white")
    my_turtle_cursor.dot(35)


def goto_second_position():
    my_turtle_cursor.penup()
    my_turtle_cursor.forward(20)
    my_turtle_cursor.right(90)
    my_turtle_cursor.forward(10)
    my_turtle_cursor.right(90)
    my_turtle_cursor.pendown()


def half():
    my_turtle_cursor.forward(50)
    draw_side_curve_of_python_logo()
    my_turtle_cursor.forward(90)
    draw_first_left_curve_of_python_logo()
    my_turtle_cursor.forward(40)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(80)
    my_turtle_cursor.right(90)
    my_turtle_cursor.forward(10)
    my_turtle_cursor.right(90)
    my_turtle_cursor.forward(120)  # on test
    draw_second_left_curve_of_python_logo()
    my_turtle_cursor.forward(30)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(50)
    draw_right_curve_of_python_logo()
    my_turtle_cursor.forward(40)
    my_turtle_cursor.end_fill()


def draw_lower_dot_of_python_logo():
    my_turtle_cursor.left(90)
    my_turtle_cursor.penup()
    my_turtle_cursor.forward(310)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(120)
    my_turtle_cursor.pendown()

    my_turtle_cursor.dot(35)


def draw_first_left_curve_of_python_logo():
    draw_side_curve_of_python_logo()
    my_turtle_cursor.forward(80)
    draw_side_curve_of_python_logo()


def draw_second_left_curve_of_python_logo():
    draw_side_curve_of_python_logo()
    my_turtle_cursor.forward(90)
    draw_side_curve_of_python_logo()


def draw_side_curve_of_python_logo():
    for i in range(90):
        my_turtle_cursor.left(1)
        my_turtle_cursor.forward(1)


def draw_right_curve_of_python_logo():
    for i in range(90):
        my_turtle_cursor.right(1)
        my_turtle_cursor.forward(1)


# Setting The configuration of our cursor according to our needs
my_turtle_cursor.pensize(2)
my_turtle_cursor.speed(10)
my_turtle_cursor.pensize(2)
my_turtle_cursor.pencolor("black")

# We have changed background color of canvas
my_turtle_screen.bgcolor("white")

# Setting the fill color of upper part python logo
my_turtle_cursor.fillcolor("#306998")

# Starting to fill color of upper part of python logo
my_turtle_cursor.begin_fill()

half()

# Stooping the cursor to fill color in upper part of python logo
my_turtle_cursor.end_fill()

goto_second_position()

# Setting the fill color of lower part of python logo
my_turtle_cursor.fillcolor("#FFD43B")
my_turtle_cursor.begin_fill()

half()

# Stooping the cursor to fill color in lower part of python logo
my_turtle_cursor.end_fill()

# Drawing upper and lower dots of python logo
draw_upper_dot_of_python_logo()
draw_lower_dot_of_python_logo()
pause()