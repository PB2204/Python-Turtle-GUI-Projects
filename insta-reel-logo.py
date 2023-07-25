import turtle as t
t.speed(100)
t.bgcolor('#fb3958')
t.pencolor('white')
t.pensize(10)
t.penup()
t.goto(100,100)
t.pendown()
t.left(180)
def border():
    t.forward(150)
    for i in range(90):
        t.forward(1)
        t.left(1)

border()
border()
border()
border()

t.penup()
# Creating A Horizontal Line and One Diagonal Line
for i in range(90):
    t.backward(1)
    t.right(1)
t.left(90)
t.pendown()
t.forward(259)
t.penup()
t.right(180)
t.forward(85)
t.left(120)
t.pendown()
t.forward(60)
t.right(120)

# Draw another Diagonal Line
t.penup()
t.forward(100)
t.right(60)
t.pendown()
t.forward(60)

#Draw a Triangle
t.penup()
t.goto(5,-20)
t.left(60)
t.right(90)
t.pendown()
for i in range(3):
    t.forward(70)
    t.left(120)
t.hideturtle()
t.done()