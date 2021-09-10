import turtle
import time
import random


delay=0.1
score=0
high_score=0

wn=turtle.screen()
wn.title("snake game")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("white")
head.penup()
head.goto(0,0)
head.direction="stop"

food=turtle.Turtle()
colors=random.choice(['red','blue','green'])
shapes=random.choice(['square','triangle','circle'])
food.speed(0)
food.shapes(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

segments=
