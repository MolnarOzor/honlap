from turtle import *
speed(-100)
def otszog(a):
    for i in range(0,5):
        forward(a)
        right(72)
def alap(a):
    otszog(a)
    left(108)
    otszog(a)

def négyes(a):
    for i in range(0,4):
        alap(a)
        right(108)
        forward(a)
        right(54)
        forward(a)
        left(72)
        forward(a)
        left(72)

def mozaik(sor,oszlop,a):
    for i in range(0,sor):
        x = xcor()
        y = ycor()
        for j in range(0,oszlop):
            négyes(a)
            forward(a)
            right(54)
            forward(a)
            left(72)
            forward(a)
            right(36)
            forward(a)
            left(72)
            forward(a)
            right(54)
            meret = ((xcor()-x)/oszlop)
        up()
        setpos(x,y-meret)
        down()

mozaik(4,4,20)
