from turtle import *


class objeto():
    def __init__(self):
        self.quadrado
        self.triangulo
        self.pentagono


    def quadrado(self):
        setup(480,360)
        for _ in range(4):
            forward(100)
            left(90)
        done()


    def triangulo(self):
        setup(480,360)
        for _ in range(3):
            forward(100)
            left(120)
        done()


    def pentagono(self):
        setup(480, 360)
        for _ in range(5):
            forward(100)
            left(72)
        done()


    def hexagono(self):
        setup(480,360)
        for _ in range(6):
            forward(100)
            left(60)
        done()


    def circulo(self):
        setup(480,360)
        circle(50)
        done()


    def desenho(self):
        speed(30)
        color("#8A2BE2")
        setup(480,360)
        for _ in range(150):
            forward(120)
            left(133)
        done()
