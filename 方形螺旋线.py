from turtle import *
tracer(True)            # 打开动画跟踪绘制图像
shape('turtle')         # 选择绘图指针形状为小海龟 
dist = 6                # 指针初始移动长度为6像素
for i in range(100):    # 循环100次
    fd(dist)            # forward()的简称
    rt(90)              # right()的简称
    dist += 6
