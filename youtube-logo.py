import turtle as t

t.pencolor('red')
t.fillcolor('red')
t.begin_fill()
t.penup()
t.goto(150,100)
t.left(180)
t.right(3)
t.pendown()

t.Screen().bgcolor('yellow')

for i in  range(10):
    t.forward(30)
    t.left(0.5)

for i in range(65):
    t.forward(1)
    t.left(1)

for i in range(6):
    t.forward(2)
    t.left(2)

for i in range(8):
    t.forward(10)
    t.left(1)

for i in range(10):
    t.left(1)
    t.forward(10)

for i in range(6):
    t.forward(2)
    t.left(2)

for i in range(65):
    t.forward(1)
    t.left(1)

t.left(3)

for i in  range(10):
    t.forward(30)
    t.left(0.5)

for i in range(65):
    t.forward(1)
    t.left(1)

for i in range(6):
    t.forward(2)
    t.left(2)

for i in range(8):
    t.forward(10)
    t.left(1)

for i in range(10):
    t.left(1)
    t.forward(10)

for i in range(65):
    t.forward(1)
    t.left(1)

for i in range(6):
    t.forward(2)
    t.left(2)

t.end_fill()
t.pencolor('white')
t.penup()
t.goto(0,0)
t.goto(-27,13)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.left(93)

for i in range(3):
    t.forward(100)
    t.left(120)

t.end_fill()
t.done()