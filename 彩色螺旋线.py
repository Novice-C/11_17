import turtle
import time
turtle.pensize(1)
turtle.speed(0)                 # 画笔速度
turtle.bgcolor("black")         # 背景为黑色
colors = ["red","yellow","purple","blue"]
#turtle.tracer(False)           # 不显示路径
for x in range(150):            # x为循环次数
    turtle.forward(5*x)        # 每次增加5像素
    turtle.color(colors[x % 4])
    turtle.left(95)             # 旋转95度
turtle.tracer(True)

