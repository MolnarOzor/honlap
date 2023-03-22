from turtle import *
colormode(255)
pensize(30)
for i in range(0,255,5):
    color(255,i,0)
    forward(1)
for i in range(0,255,5):
    color(255-i,255,0)
    forward(1)
for i in range(0,255,5):
    color(0,255,i)
    forward(1)
for i in range(0,255,5):
    color(0,255-i,255)
    forward(1)

