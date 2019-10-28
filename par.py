import sys
from math import pi

cadena_leída = input("ingresa el radio")
radio = float (cadena_leída)

volumen = 4 / 3 * pi * radio ** 3

print (round (volumen, 3))