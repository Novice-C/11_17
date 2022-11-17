import turtle as t
import random

t.colormode(255)
t.speed(0)
t.bgcolor("black")
t.pensize(200)
t.goto(-1000,400)
t.forward(2000)

t.penup()
t.goto(-1000,200)
t.pencolor(50,50,50)
t.pendown()
t.forward(2000)

t.penup()
t.goto(-1000,0)
t.pencolor(75,75,75)
t.pendown()
t.forward(2000)

t.penup()
t.goto(-1000,-200)
t.pencolor(90,90,90)
t.pendown()
t.forward(2000)

t.penup()
t.goto(-1000,-400)
t.pencolor(115,115,115)
t.pendown()
t.forward(2000)

t.penup()
t.goto(-1000,-600)
t.pencolor(140,140,140)
t.pendown()
t.forward(2000)



t.pensize(2)
 
for i in range(50):
    x=random.randint(-800,800)
    y=random.randint(-200,400)
    
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    
    t.penup()
    t.goto(x,y)
    t.pendown()
    
    t.begin_fill()

    t.color(red,green,blue)
    
    
    for i in range(4):
        t.forward(50)
        t.left(30)
        t.forward(50)
        t.right(120)
    t.left(40)
    t.end_fill()
    
