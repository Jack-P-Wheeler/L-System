from turtle import *
from random import *
from math import *

angle = 30
axiom = "X"

generator = {"X": "D+[--DB]D[+DB]-X",
             "P": "[-F++F++++F++F]",
             "B": "PZPZPZPZ",
             "Z": "Y",
             "Y": "+++",
             "D": "DFF"}

screensize(1000,800)
speed(0)


def create_string(axiom, generator, order):
    newFractal = axiom
    for j in range(order):
        tempFractal = ""
        for i in range(len(newFractal)):
            if newFractal[i] in generator:
                tempFractal += generator[newFractal[i]]
            else:
                tempFractal += newFractal[i]
        newFractal = tempFractal
    return newFractal

def draw_fractal(fractal, D):
    n = 0
    positions = []
    for i in range(len(fractal)):
        if fractal[i] == 'F':
            fd(D)
        elif fractal[i] == 'f':
            pu()
            fd(D)
            pd() 
        elif fractal[i] == '+':
            right(angle)
        elif fractal[i] == '-':
            left(angle)
        elif fractal[i] == '[':
            positions.append([pos(), heading(), D])
        elif fractal[i] == ']':
            turtleState = positions.pop()
            pu()
            setpos(turtleState[0][0], turtleState[0][1])
            seth(turtleState[1])
            D = turtleState[2]
            pd()
    
left(90)
pu()
sety(-300)
setx(0)
pd()


new_fractal = create_string(axiom, generator, 6)
draw_fractal(new_fractal, 5)

done()