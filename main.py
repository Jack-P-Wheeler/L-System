from math import *
from Lsystem import *


screensize(1000,800)
speed(0)

#Pull request test
        
left(90)
pu()
sety(-350)
setx(0)
pd()


angle = 20
distance = 5
axiom = "F0F1F1"

generator = [["0", ["1", "0", "0"]],
             ["0", ["0", "0", "1"]],
             ["1", ["0", "0", "0"]],
             ["1", ["1F1", "0", "1"]],
             ["0", ["1", "1", "0"]],
             ["0", ["1[+F1F1]", "1", "1"]],
             ["1", ["1", "1", "0"]],
             ["1", ["0", "1", "1"]],
             ["+", ["-", "*", "*"]],
             ["-", ["+", "*", "*"]]]

new_fractal = create_string(axiom, generator, 26)
draw_fractal(new_fractal, distance, angle)
print(new_fractal)
print(len(new_fractal))


done()