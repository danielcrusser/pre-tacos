"""i = 0
while i <= 3:
	print(i)
	i += 1
print ("hecho")
"""

from math import sqrt

x = float(input("introduce un numero positivo"))
while x < 0:
	x = float(input("introduce un numero positivo"))

print(" la raiz cuadrada de {0} es {1}".format(x, sqrt(x)))