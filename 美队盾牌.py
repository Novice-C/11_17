import turtle as t
t.speed()

t.penup()
t.goto(0,-200)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(200)
t.end_fill()

t.penup()
t.goto(0,-165)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(165)
t.end_fill()

t.penup()
t.goto(0,-130)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(130)
t.end_fill()

t.penup()
t.goto(0,-75)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.circle(75)
t.end_fill()

t.penup()
t.goto(-50,15)
t.pendown()
t.fillcolor("white")
t.begin_fill()
for i in range(5):
    t.forward(100)
    t.right(144)
t.end_fill()



