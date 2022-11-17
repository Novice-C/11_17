import turtle as t
import random

t.speed(0)

t.colormode(255)
for i in range(10):
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    x = random.randint(-800,500)
    y = random.randint(-500,500)

    
    t.penup()
    t.goto(x,y)
    t.pendown()

    t.color(red,green,blue)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.begin_fill()




    





