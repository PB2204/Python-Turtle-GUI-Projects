import turtle as t
t.bgcolor("white")
t.penup()
t.goto(-80,80)
t.pendown()

t.speed(8)
t.pencolor("#3DDC84")
    
def circle():
    t.begin_fill()
    t.fillcolor('white')
    t.circle(7)
    t.end_fill()
#Drawing the Head
def draw_upperbody():
    t.begin_fill()
    t.fillcolor("#3DDC84")
    t.forward(150)
    t.left(90)

    for i in range(238):
        t.left(0.76)
        t.forward(1)
    t.end_fill()
    
    #drawing eyes
    #left Eye
    t.penup()
    t.goto(-46,120)
    t.pendown()
    circle()
    
    #Right Eye
    t.penup()
    t.goto(24,120)
    t.pendown()
    circle()
    
    #Drawing ears
    #left ear
    t.penup()
    t.goto(-40,140)
    t.pendown()

    t.pensize(4)
    t.right(140)
    t.forward(50)

    #Right ear
    t.penup()
    t.goto(34,144)
    t.pendown()

    t.pensize(4)
    t.right(80)
    t.forward(46)
    
#Drawing the middle body
def draw_middlebody():
    t.begin_fill()
    t.fillcolor("#3DDC84")
    t.pensize(1)

    t.right(141)
    t.forward(100)

    for i in range(20):

        t.forward(1)
        t.left(5)
    t.right(9.5)
    t.forward(127)

    for i in range(20):
        t.forward(1)
        t.left(5)
    t.right(9.5)
    t.forward(100)
    t.end_fill()

#hand
def draw_hand():
    t.begin_fill()
    t.fillcolor("#3DDC84")
    for i in range(45):
        t.right(4)
        t.forward(1)
    t.forward(70)
    for i in range(45):
        t.right(4)
        t.forward(1)
    t.forward(70)
    t.end_fill()

#legs
def draw_legs():

    t.begin_fill()
    t.fillcolor("#3DDC84")
    t.right(91)
    t.forward(30)
    t.right(90)
    t.forward(50)

    for i in range(45):
        t.right(4)
        t.forward(1)

    t.end_fill()


draw_upperbody()

t.penup()
t.goto(-80,68)
t.pendown()

draw_middlebody()

t.penup()
t.goto(80,68)
t.pendown()

draw_hand()

t.penup()
t.goto(-124,70)
t.pendown()

draw_hand()

t.penup()
t.goto(-50,-50)
t.pendown()

draw_legs()

t.penup()
t.goto(14,-50)
t.pendown()
t.left(1.7)
draw_legs()


t.hideturtle()

t.done()