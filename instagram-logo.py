from turtle import * #importing the module

def backFrame():
    COLOR = (0.60156, 0, 0.99218)  # (154, 0, 254)
    TARGET = (0.86328, 0.47656, 0.31250)  # (221, 122, 80)

    screen = Screen()
    screen.tracer(False)

    WIDTH, HEIGHT = screen.window_width(), screen.window_height() #defining some useful variables

    deltas = [(hue - COLOR[index]) / HEIGHT for index, hue in enumerate(TARGET)]

    turtle = Turtle()
    turtle.color(COLOR)

    turtle.penup()
    turtle.goto(-WIDTH/2, HEIGHT/2)
    turtle.pendown()

    direction = 1

    #the gradient background
    for distance, y in enumerate(range(HEIGHT//2, -HEIGHT//2, -1)):

        turtle.forward(WIDTH * direction)
        turtle.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
        turtle.sety(y)

        direction *= -1

    screen.tracer(True)

def main():
    ## setting all the pre-defined values to be used in the program
    pen_color = 'white'
    width_val = 23
    round_coordA, round_coordB = 34, 90
    circleAx, circleAy = 80, 360
    circleBx, circleBy = 7, 360
    gotoAx, gotoAy = 85, 30
    gotoBx, gotoBy = 160, -100

    pencolor(pen_color) #defining the color of the pen
    width(width_val) #defining the thickness of the pen
    penup() #start the draw
    goto(gotoBx, gotoBy) #set the origin for the graphics
    pendown() #stop the draw temporarily

    left(90) #turn at an angle
    for i in range(4): #loop for 4 times for a square-type shape
        forward(250)
        circle(round_coordA, round_coordB) #for border-radius

    penup() # for the big circle
    goto(gotoAx, gotoAy) # defining the new origin for the pen
    pendown() # stopping the draw
    circle(circleAx, circleAy) #built-in function for a circle in the middle

    penup()
    goto(110,130) # setting the new origin
    pendown()
    circle(circleBx, circleBy) # built-in function for a circle at the top-right

    done() # end the program

if __name__ == "__main__":
    backFrame()
    main()