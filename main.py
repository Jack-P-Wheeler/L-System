from math import *
from Lsystem import *
from random import *

def setupTurtle():
    screensize(1000,800)
    speed(0)
    left(90)
    pu()
    sety(-350)
    setx(0)
    pd()

def mutateGenome(genomeA, genomeB):
    from Lsystem import rule
    newGenome = []
    if len(genomeA) != len(genomeB):
        return None
    for i in range(len(genomeA)):
        newSeed = str(genomeA[i].seed if random() > 0.5 else genomeB[i].seed)
        newLeft = str(genomeA[i].left if random() > 0.5 else genomeB[i].left)
        newRight = str(genomeA[i].right if random() > 0.5 else genomeB[i].right)
        newSprout = str(genomeA[i].sprout)
        newGenome.append(rule(newSeed, newSprout, newLeft, newRight))
    return newGenome


angle = 16
length = 20
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
for i in range(16):
    new_fractal = replaceString(new_fractal, genome)

print(stripChars(new_fractal, ('1', '0')))
setupTurtle()
drawFractal(new_fractal, length, angle)