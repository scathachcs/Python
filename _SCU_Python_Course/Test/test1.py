import turtle;

turtle.setup(width=800,height=800)
turtle.pencolor("black") 

turtle.fillcolor("blue")        #绘制海面
turtle.penup()
turtle.goto(-400,0)
turtle.begin_fill()
turtle.pendown()
turtle.seth(0)
turtle.forward(800)
turtle.seth(270)
turtle.forward(400)
turtle.seth(180)
turtle.forward(800)
turtle.seth(90)
turtle.forward(400)
turtle.end_fill()

turtle.fillcolor("red")          #绘制太阳
turtle.penup()
turtle.goto(-200,0)
turtle.begin_fill()
turtle.pendown()
turtle.seth(90)
turtle.circle(-200,180)
turtle.seth(180)
turtle.forward(400)
turtle.end_fill()

turtle.done()