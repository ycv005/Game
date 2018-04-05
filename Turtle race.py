import turtle           #importing turtle module
import random           #importing random module
s=turtle.Screen()       #creating the graphic window
r=turtle.Turtle()       #turtle with name "r"
r.speed(10)              #speed of the turtle(r) is 6 unit
r.penup()               #penup, is used when we don't want to create line when our turtle is moving
r.goto(-100,50)           #100 as x coordinate and 50 as y cordinate in graphic window. Remember, that it goes to that point with 
x=20

for i in range(15):     
    r.write(i)          #it writes the value which comes as argument
    r.right(90)         #turtle turn by 90 degree
    r.pendown()
    for i in range(10):         #for dash lines
        r.forward(10)
        r.penup()
        r.forward(10)
        r.pendown()
    r.penup()           
    r.goto(-100+x,50)
    x=x+25
    r.left(90)          #turtle turn by 90 degree left

r.goto(-150,30)
r.pendown()
r.write('Anshu')
r.penup()

anshu=turtle.Turtle()   #2nd turtle with name anshu
anshu.color('red')      #turtle color- red
anshu.shape('turtle')   #shape is- turtle, available shape-“arrow”, “circle”, “square”, “triangle”, “classic”
anshu.penup()
anshu.goto(-100,35)       #jumping to the 100,35 coordinate
for t in range(5):              #rotating the turtle by 360
    anshu.right(72)

r.goto(-150,0)
r.pendown()
r.write('Abhi')
r.penup()

abhi=turtle.Turtle()
abhi.color('green')
abhi.shape('turtle')
abhi.penup()
abhi.goto(-100,5)
for t in range(5):
    abhi.right(72)

r.goto(-150,-30)
r.pendown()
r.write('Shiv')
r.penup()

shiv=turtle.Turtle()
shiv.color('yellow')
shiv.shape('turtle')
shiv.penup()
shiv.goto(-100,-25)
for t in range(5):
    shiv.right(72)

r.goto(-150,-55)
r.pendown()
r.write('Amit')
r.penup()

amit=turtle.Turtle()
amit.color('blue')
amit.shape('turtle')
amit.penup()
amit.goto(-100,-50)
for t in range(5):
    amit.right(72)

r.goto(-150,-80)
r.pendown()
r.write('Jatin')
r.penup()

Jatin=turtle.Turtle()
Jatin.color('black')
Jatin.shape('turtle')
Jatin.penup()
Jatin.goto(-100,-75)
for t in range(5):
    Jatin.right(72)

r.goto(-150,-105)
r.pendown()
r.write('Pratik')
r.penup()

pratik=turtle.Turtle()
pratik.color('#f99c39')
pratik.shape('turtle')
pratik.penup()
pratik.goto(-100,-100)
for t in range(5):
    pratik.right(72)

r.goto(-150,-130)
r.pendown()
r.write('Aman')
r.penup()

aman=turtle.Turtle()
aman.color('lightgreen')
aman.shape('turtle')
aman.penup()
aman.goto(-100,-125)
for t in range(5):
    aman.right(72)

#When every player setup, know, let them leave path on running
pratik.pendown()
Jatin.pendown()
shiv.pendown()
amit.pendown()
aman.pendown()
anshu.pendown()
abhi.pendown()

for i in range(110):
    anshu.forward(random.randint(1,5))      #intruction given to each turtle to move forward such that their movement depend on luck 
    abhi.forward(random.randint(1,5))
    shiv.forward(random.randint(1,5))
    Jatin.forward(random.randint(1,5))
    amit.forward(random.randint(1,5))
    pratik.forward(random.randint(1,5))
    aman.forward(random.randint(1,5))

s.exitonclick()     #hold the graphic window, until we close it.
