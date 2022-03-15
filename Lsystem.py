from turtle import *
from random import *
from math import *

def create_string(axiom, generator, order):
    newFractal = axiom 
    for j in range(order):
        tempFractal = ""
        for i in range(len(newFractal)):
            found = False
            if newFractal[i] in generator and []:
                contextL = generator[newFractal[i]][1]
                contextR = generator[newFractal[i]][2]
                if [contextL, contextR] == context_search(newFractal, i, contextL, contextR) or contextL == "*" or contextR == "*":
                    found = True
                    tempFractal += generator[newFractal[i]][0]
            if found == False:
                tempFractal += newFractal[i]
        newFractal = tempFractal
    return newFractal

def context_search(tempString, i, searchL, searchR):
    return [realContextL, realContextR]

def draw_fractal(fractal, D, angle):
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
            
def random_fractals(axiom, generator, maxOrder, D, angle, amount):
    for z in range(amount):
        new_fractal = create_string(axiom, generator, round(random() * maxOrder))
        pu()
        sety(random() * 700 - 350)
        setx(random() * 900 - 450)
        seth(90)
        pd()    
        draw_fractal(new_fractal, D, angle)