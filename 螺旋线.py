import turtle as t
t.bgcolor("black")
sides = eval(input("请输入你要绘制的多边形，请输入2-7的数字："))
colors=["red","yellow","green","blue","orange","purple","pink"]
t.speed(0)
t.pensize(10)

for x in range(700):
    t.pencolor(colors[x%sides])
    t.left(360/sides+1)
    t.width(x*sides/100)            #线条越来越宽
    t.forward(2*x)
   
