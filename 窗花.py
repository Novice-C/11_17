from turtle import *
pensize(5)
speed(0)
bgcolor("pink")
def arc(initial_degree,range_num,step,rotate_degree):
    setheading(initial_degree)
    for n in range(range_num):
        forward(step)
        right(rotate_degree)

initial_degree = 0
for i in range(9):
    pu()
    home()
    pd()
    pencolor("green")
    arc(40*i,120,4,3)
