from math import *
from Lsystem import *


screensize(1000,800)
speed(0)


#left(90)
#pu()
#sety(-350)
#setx(0)
#pd()


angle = 60
distance = 10
axiom = "F"

generator = [["F", ["F-F++F-F", "*", "*"]]]

new_fractal = create_string(axiom, generator, 3)
draw_fractal(new_fractal, distance, angle)


done()