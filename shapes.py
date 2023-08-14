


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

def drawHome(t):
    t.color("#000000")
    t.penup()
    t.goto(-160,-20)
    t.pendown()
    t.setheading(90)
    t.fillcolor("#ffffff")
    t.begin_fill()
    roof1 = t.position()
    t.forward(300)
    roof2 = t.positi
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.end_fill()



































