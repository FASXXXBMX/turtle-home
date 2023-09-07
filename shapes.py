


def drawSun(t,  x, y, size):
    t.setheading(0)#поворот напровлении верх
    t.fillcolor("yellow")
    t.penup()#ручкаверх
    t.goto(x,y)#переход x y
    t.pendown()#ручкавнис
    t.begin_fill()#рисовать внутриности крга
    t.circle(size)# circle - круг, рисуем круг передавая размер который содержиться size
    t.end_fill()# закончить закрашивание замкнутной фигуры
def drawCloud(t, x, y):
    t.setheading(90)
    t.fillcolor("white")
    t.penup()#ручкаверх
    t.goto(x, y)  # переход x
    t.pendown()  # ручкавнис
    t.begin_fill()  # рисовать внутриности крга

    t.color("white")
    for x in range(10):
        t.circle(20)#РИСУЕТкруг
        t.right(36)
        t.forward(10)
    t.end_fill()
    t.setheading(90)

def drawGrass(t):
    t.setheading(90)
    t.fillcolor("#05ff05")
    t.penup()
    t.setheading(90)
    t.goto(-700,-500)
    t.begin_fill()

    for x in range(2):
        t.forward(300)
        t.right(90)
        t.forward(10000)
        t.right(90)
    t.end_fill()
    t.setheading(90)

def drawBush(t, x, y):
    t.setheading(90)
    t.fillcolor("#00ff6f")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()

    t.color("#00ff6f")
    for x in range(10):
        t.circle(20)
        t.right(36)
        t.forward(10)
    t.end_fill()
    t.setheading(90)

def drawHome(pen):
    pen.color(0,0,0)
    pen.penup()
    pen.goto(-200,-200)
    pen.pendown()
    pen.setheading(90)
    pen.fillcolor("white")
    pen.begin_fill()
    pen.forward(150)
    roof1=pen.position()
    pen.right(90)
    pen.forward(300)
    roof2 = pen.position()
    pen.right(90)
    pen.forward(150)
    pen.right(90)
    pen.forward(300)
    pen.right(90)
    pen.end_fill()

#roof

    pen.goto(roof1)
    pen.fillcolor('#8a8a8a')#внутреносте
    pen.begin_fill()
    pen.pendown()
    pen.goto(-30,20)
    pen.goto(roof2)
    pen.goto(roof1)
    pen.end_fill()
    pen.setheading(90)

def drawdoor(pen, x ,y):
    pen.penup()
    pen.goto(x ,y)
    pen.fillcolor("#5c0606")
    pen.begin_fill()
    pen.setheading(90)





    for x in range(2):
        pen.forward(50)
        pen.right(90)
        pen.forward(30)
        pen.right(90)
















































