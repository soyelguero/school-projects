import turtle
t = turtle
s = t.Screen()

#turtle settings
t.mode('logo')
t.hideturtle()
s.screensize(800, 800)
t.speed('normal')
s.bgcolor('white')
t.pencolor("black")
t.fillcolor("red")
t.shape('classic')



b = turtle
b.mode('logo')
b.up()
b.setposition(-40, -20)
b.seth(20)
b.width(width=9)
b.down()

#tail
b.begin_fill()
b.seth(-160)
b.forward(5)
b.seth(-340)
b.forward(20)
b.seth(-200)
b.forward(20)
b.seth(-90)
b.forward(5)
b.end_fill()

b.seth(0)

#body
b.circle(-20, 360/11)
b.width(width=8)
b.circle(80, 360/6)
b.width(width=11)
b.circle(-80, 360/8)
b.width(width=13)
b.circle(-80,360/10)
b.width(width=10)
b.circle(80,360/8)

#head
b.begin_fill()
b.seth(90)
b.forward(20)
b.seth(340)
b.forward(60)
b.seth(200)
b.forward(60)
b.seth(90)
b.forward(20)
b.end_fill()




t.exitonclick()

