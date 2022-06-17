from math import *
from Lsystem import *

def setupTurtle():
    screensize(1000,800)
    speed(0)
    left(90)
    pu()
    sety(-350)
    setx(0)
    pd()

angle = 16
distance = 10
axiom = "F1F1F1"

genome =   [rule('0', '0', '0', '0'),
            rule('0', '1[+F1F1]', '0', '1'),
            rule('1', '1', '0', '0'),
            rule('1', '1', '0', '1'),
            rule('0', '0', '1', '0'),
            rule('0', '1F1', '1', '1'),
            rule('1', '0', '1', '0'),
            rule('1', '0', '1', '1'),
            rule('+', '-', '*', '*'),
            rule('-', '+', '*', '*')]

new_fractal = axiom
for i in range(14):
    new_fractal = replaceString(new_fractal, genome)
setupTurtle()
drawFractal(new_fractal, distance, angle)