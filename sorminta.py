from turtle import *
import math
def teglalap(a,b,szin):
    fillcolor(szin)
    begin_fill()
    for i in range(0,2):
        forward(a)
        right(90)
        forward(b)
        right(90)
    end_fill()

def haromszog(a,szin):
    fillcolor(szin)
    begin_fill()
    for i in range(0,3):
        forward(a)
        right(120)
    end_fill()

setheading(90)
pensize(2)
speed(0)

def elem(h):
    teglalap(h,h/4,'green')
    up()
    setpos(xcor()+h/4,ycor()+h/4)
    down()
    haromszog(h/2,'red')
    up()
    setpos(xcor()+h*math.sqrt(3)/4,ycor()-h/4)
    down()
    teglalap(h/2,h/2,'orange')
    setpos(xcor()+h/2,ycor())
    teglalap(h,h/4,'green')

def egyik (db,h):
    for i in range(0,db):
        elem(h)


egyik(20,20)



