import turtle

from shapes import *

t = turtle.Turtle()


t.speed(100)


screen = turtle.Screen()
screen.colormode(255)

t.color(0,0,0)
wn = turtle.Screen()
wn.bgcolor(66,202,244)

drawSun(t,-200,160,70)
drawCloud(t,75,160)
drawGrass(t)
drawBush(t,75,-150)
drawHome(t)
drawdoor(t,0,-200 )
drawGARAGE(t, -100 , -200 , "square")

turtle.done()

