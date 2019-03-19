import math

# Função é y = 3*x**2 - 4*x - 10, logo:
a = 3
b = -4
c = -10

# Primeiramente devemos calcular delta:
delta = (b**2)-4*a*c

# Para então obter os zeros da função:
x1 = (-b+math.sqrt(delta))/(2*a)
x2 = (-b-math.sqrt(delta))/(2*a)
print('as raízes são', x1, 'e', x2)
