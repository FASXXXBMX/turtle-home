import turtle

t = turtle.Turtle()

#def drawSun(t,  x, y, size):
#    t.setheading(0)#поворот напровлении верх
#    t.fillcolor("yellow")
#    t.penup()#ручкаверх
#    t.goto(x,y)#переход x y
#    t.pendown()#ручкавнис
#    t.begin_fill()#рисовать внутриности крга
#    t.

def drawBush(t,x,y):
    t.setheading(90)
    t.fillcolor("#00ff6f")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()

    t.color("#00ff6f")
    for x in range(10):
        t.circle(20)
        t.right(36)
        t.forward(10)
    t.end_fill()
    t.setheading(90)

drawBush(t,0,0)

turtle.done()
