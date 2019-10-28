import math 

#RAIZ CUADRADA MEDIANTE:    FORMULA DE HERÓN

a = float(input("ingresa el lado A: "))
b = float(input("ingresa el lado B: "))
c = float(input("ingresa el lado C: "))

per = a+b+c
s =  per / 2
suma = s * (s-a) * (s-b) * (s-c) 
numraiz = abs(suma)


print("el perimetro es: ", per, "el area es: ", math.sqrt( numraiz))
 