from turtle import *
setheading(90)
speed(0)
def tégla(h):
    for i in range(0,2):
        forward(h)
        right(90)
        forward(2*h)
        right(90)

def forgó(db,h):
    for i in range(0,db):
        tégla(h)
        right(360/db)

def pikkely(r):
    circle(r ,extent=180)
    left(90)
    circle(-r, extent=90)
    right(180)
    circle(-r, extent=90)

def sor (db,r):
    for i in range(db):
        pikkely(r)
        left(180)
        circle(r, extent=90)
        left(180)



#forgó(7,50)
sor(3,100)
