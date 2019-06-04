# AULA 10, EXERCÍCIO 3

import numpy as np
from math import pi, sin, cos
import matplotlib.pyplot as plt

# 1) Integral de sin(x), com 0 <= x <= 2pi:
I = cos(0)-cos(2*pi)
print 'Integral de sin(x), com 0 <= x <= 2pi, vale:', round(I,5)

# Definindo os valores de x, y e plotando o gráfico em barras:
x=np.linspace(0,2*pi,50)
y=[sin(xi) for xi in x]
plt.bar(x,y,color="red",align="center",width=2*pi/50)

# Definindo os valores de x1, y1 e plotando a curva:
x1=np.linspace(0,2*pi,100)
y1=[sin(xi) for xi in x1]
plt.plot(x1,y1)
plt.title('Grafico de sin(x)',fontsize=14)
plt.xlabel('x',fontsize=12)
plt.ylabel('sin(x)',fontsize=12)
plt.show()

# Verificando se a soma de Riemann das barras é aproximadamente zero, que é o valor da integral:
S = 0
for xi in x:
    S = S + sin(xi)*2*pi/50 
    
print 'Soma das 50 barras =', round(S,5)

S1= 0
for xi in x1:
    S1 = S1 + sin(xi)*2*pi/100
print 'Soma das 100 barras = ', round(S1,5), '\n'

# 2) Integral de cos(x), com 0 <= x <= 2pi:
I = sin(2*pi)-sin(0)
print 'Integral de cos(x), com 0 <= x <= 2pi, vale:', round(I,5)

# Definindo os valores de x, y e plotando o gráfico em barras:
x=np.linspace(0,2*pi,500)
y=[cos(xi) for xi in x]
plt.bar(x,y,color="red",align="center",width=2*pi/500)

# Definindo os valores de x1, y1 e plotando a curva:
x1=np.linspace(0,2*pi,1000)
y1=[cos(xi) for xi in x1]
plt.plot(x1,y1)
plt.title('Grafico de cos(x)',fontsize=14)
plt.xlabel('x',fontsize=12)
plt.ylabel('cos(x)',fontsize=12)
plt.show()

# Verificando se a soma de Riemann das barras é aproximadamente zero, que é o valor da integral:
S = 0
for xi in x:
    S = S + cos(xi)*2*pi/500
    
print 'Soma das 500 barras =', round(S,5)

S1= 0
for xi in x1:
    S1 = S1 + cos(xi)*2*pi/1000
print 'Soma das 1000 barras = ', round(S1,5)
