from turtle import *
from random import *

def moveToRandomLocation():
    penup()
    setpos(randint(-400, 400), randint(-400, 400))
    pendown()

def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        forward(starSize)
        left(144)
    end_fill()
    penup()

# função para desenhar uma pequena galáxia de estrelas
def drawGalaxy(numberOfStars):
    starColours = ["#058396", "#027546", "#827E01"]
    moveToRandomLocation()
    # desenha várias pequenas estrelas coloridas
    for star in range(numberOfStars):
        penup()
        left(randint(-180, 180))
        forward(randint(5, 20))
        pendown()
        drawStar(2, choice(starColours))

def drawConstellation(numberOfStars):
    moveToRandomLocation()
    for star in range(numberOfStars):
        drawStar(randint(7, 15), "white")
        pendown()
        left(randint(-90, 90))
        forward(randint(30, 70))

bgcolor("MidnightBlue")

for star in range(30):
    moveToRandomLocation()
    drawStar(randint(5, 25), "White")

for galaxy in range(3):
    drawGalaxy(40)

for constellation in range(2):
    drawConstellation(randint(4, 7))

hideturtle()
done()
