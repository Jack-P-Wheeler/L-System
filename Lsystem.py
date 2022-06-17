from turtle import *
from random import *
from math import *

class rule:
    def __init__(self, seed, sprout, left, right):
        self.seed = seed
        self.sprout = sprout
        self.left = left
        self.right = right

def replaceString(axiom, generator):
    newFractal = ""
    for i in range(len(axiom)):
        for rule in generator:
            replaced = False
            if axiom[i] == rule.seed and (rule.left == contextSearch(axiom, i)[0] or rule.left == "*") and (rule.right == contextSearch(axiom, i)[1] or rule.right == "*"):
                newFractal += rule.sprout
                replaced = True
                break
        if replaced != True:
            newFractal += axiom[i]
    return newFractal

def contextSearch(tempString, pos):
    realContextL, realContextR = None, None
    ignore = ["F", "+", "-", "[", "]"]
    r, l = pos, pos

    branchCounter = 0
    while r < len(tempString) - 1 and realContextR is None:
        r += 1
        if tempString[r] == "]" and branchCounter == 0:
            realContextR = None
        if tempString[r] == "[":
            branchCounter += 1
        if tempString[r] == "]" and branchCounter > 0:
            branchCounter -= 1
        if (tempString[r] not in ignore) and branchCounter == 0:
            realContextR = tempString[r]

    branchCounter = 0
    while l > 0 and realContextL is None:
        l -= 1
        if tempString[l] == "]":
            branchCounter += 1
        if tempString[l] == "[" and branchCounter > 0:
            branchCounter -= 1
        if (tempString[l] not in ignore) and branchCounter == 0:
            realContextL = tempString[l]
        
    return [realContextL, realContextR]

def drawFractal(fractal, D, angle):
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
    done()