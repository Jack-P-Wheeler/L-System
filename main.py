from math import *
from Lsystem import *


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

generator = [["0", ["0", "0", "0"]],
             ["0", ["1[+F1F1]", "0", "1"]],
             ["1", ["1", "0", "0"]],
             ["1", ["1", "0", "1"]],
             ["0", ["0", "1", "0"]],
             ["0", ["1F1", "1", "1"]],
             ["1", ["0", "1", "0"]],
             ["1", ["0", "1", "1"]],
             ["+", ["-", "*", "*"]],
             ["-", ["+", "*", "*"]]]

new_fractal = create_string(axiom, generator, 20)
draw_fractal(new_fractal, distance, angle)

done()