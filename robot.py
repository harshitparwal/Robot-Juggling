# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:11:54 2020

@author: asus
"""

import turtle as t
from turtle import Screen
r=t.Turtle()
l=t.Turtle()
m=t.Turtle()
m.hideturtle()
r.hideturtle()
l.hideturtle()
screen= Screen()

def rectangle(h,v,col):
    t.pendown()
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for counter in range(2):
        t.forward(h)
        t.right(90)
        t.forward(v)
        t.right(90)
    t.end_fill()
    t.penup()


#background

t.penup()
t.speed('normal')
t.bgcolor('grey')

#feet

t.penup()
t.goto(-100,-150)    
rectangle(50,20,"blue")
t.goto(-30,-150)
rectangle(50,20,"blue")

#legs

t.goto(-25,-50)
rectangle(15,100,"peru")
t.goto(-70,-50)
rectangle(15,100,"peru")

#body

t.goto(-90,100)
rectangle(100,150,"red")

#arms

t.goto(-150,70)
rectangle(60,15,"peru")
t.goto(10,70)
rectangle(60,15,"peru")
t.goto(-150,110)
rectangle(15,40,"peru")
t.goto(55,110)
rectangle(15,40,"peru")

#neck

t.goto(-50,120)
rectangle(15,20,"peru")

#face

t.goto(-85,170)
rectangle(80,50,"peach puff")

#eyes whitepart

t.goto(-60,160)
rectangle(30,10,"white")

#eyes blackpart

t.goto(-55,155)
rectangle(5,5,"black")
t.goto(-40,155)
rectangle(5,5,"black")

#mouth

t.goto(-65,135)
rectangle(40,5,"black")

#hideturtle

t.hideturtle()


r.penup()
l.penup()
m.penup()
r.goto(60,120)
r.shape("square")
r.showturtle()
r.speed("slow")
l.goto(-140,120)
l.shape("square")
l.speed("slow")
l.showturtle()
m.goto(-40,250)
m.shape("square")
m.showturtle()

"""for i in range(200):
    r.goto(150,120)
    r.goto(60,120)
    l.goto(-240,120)
    l.goto(-140,120)"""

while True:
    r.goto(-40,250)
    m.goto(-140,120)
    l.goto(60,120)
    r.goto(-140,120)
    m.goto(60,120)
    l.goto(-40,250)
    r.goto(60,120)
    m.goto(-40,250)
    l.goto(-140,120)

screen.exitonclick()
    


    







