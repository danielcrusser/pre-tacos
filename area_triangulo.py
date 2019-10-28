import math 
from decimal import Decimal 
from fractions import Fraction

a = float(input("ingresa el lado A: "))
b = float(input("ingresa el lado B: "))
seno = float(input("ingresa el seno: "))

rad = seno * (3.1416/180)
area = 0.5 * a * b * rad

print ("el area del triangulo es: ", round(area, 1))