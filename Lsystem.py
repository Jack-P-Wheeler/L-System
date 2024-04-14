from turtle import *
from random import *
from math import *

from matplotlib.pyplot import switch_backend

class rule:
    def __init__(self, seed, sprout, left, right):
        self.seed = seed
        self.sprout = sprout
        self.left = left
        self.right = right

class line:
    def __init__(self, start, end):
        self.start = {'x': start[0], 'y': start[1]}
        self.end = {'x': end[0], 'y': end[1]}

def replaceString(axiom, genome):
    newFractal = ""
    for i in range(len(axiom)):
        for rule in genome:
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

def drawFractal(fractal, D, angle, scale = 1):
    length = D
    positions = []
    nestCount = 0
    for i in range(len(fractal)):
        pensize(max(0, (6 - nestCount)))
        if fractal[i] == 'F':
            fd(length)
        elif fractal[i] == 'f':
            pu()
            fd(length)
            pd() 
        elif fractal[i] == '+':
            right(angle)
        elif fractal[i] == '-':
            left(angle)
        elif fractal[i] == '[':
            nestCount += 1
            positions.append([pos(), heading(), length])
            length *= scale
        elif fractal[i] == ']':
            nestCount -= 1
            turtleState = positions.pop()
            pu()
            setpos(turtleState[0][0], turtleState[0][1])
            seth(turtleState[1])
            length = turtleState[2]
            pd()
    done()

#Function that strips characters in a list from a string
def stripChars(string, chars):
    newString = ""
    for i in range(len(string)):
        if string[i] not in chars:
            newString += string[i]
    return newString