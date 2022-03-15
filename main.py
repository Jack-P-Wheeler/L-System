from turtle import *
from random import *
from math import *
from Lsystem import *


screensize(1000,800)
speed(0)


        
left(90)
pu()
sety(-300)
setx(0)
pd()


angle = 30
distance = 5
axiom = "X"

generator = {"X": ["FX", "*", "*"],
             "F": ["f", "F", "*"]}

new_fractal = create_string(axiom, generator, 20)
draw_fractal(new_fractal, distance, angle)
print(new_fractal)
print(len(new_fractal))

done()