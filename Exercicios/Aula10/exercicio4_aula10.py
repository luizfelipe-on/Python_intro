import numpy as np
from math import pi, sinh, cosh
import matplotlib.pyplot as plt

# 1) Integral de sinh(x), com 0 <= x <= 10:
I = cosh(10)-cosh(0)
print('Integral de sinh(x), com 0 <= x <= 10, vale:', round(I,5))

# Definindo os valores de x, y e plotando o gráfico em barras:
x=np.linspace(0,10,500)
y=[sinh(xi) for xi in x]
plt.bar(x,y,color="red",align="center",width=0.02)

# Definindo os valores de x1, y1 e plotando a curva:
x1=np.linspace(0,10,1000)
y1=[sinh(xi) for xi in x1]
plt.plot(x1,y1)
plt.title('Grafico de sinh(x)',fontsize=14)
plt.xlabel('x',fontsize=12)
plt.ylabel('sinh(x)',fontsize=12)
plt.show()

# Estimando o valor da integral usando a soma de Riemann das barras:
S = 0
for xi in x:
    S = S + sinh(xi)*0.02 
    
print('Soma das 500 barras =', round(S,5))

S1= 0
for xi in x1:
    S1 = S1 + sinh(xi)*0.01
print('Soma das 1000 barras = ', round(S1,5), '\n')

# 2) Integral de cosh(x), com 0 <= x <= 10:
I = sinh(10)-sinh(0)
print('Integral de cosh(x), com 0 <= x <= 10, vale:', round(I,5))

# Definindo os valores de x, y e plotando o gráfico em barras:
x=np.linspace(0,10,500)
y=[cosh(xi) for xi in x]
plt.bar(x,y,color="red",align="center",width=0.02)

# Definindo os valores de x1, y1 e plotando a curva:
x1=np.linspace(0,10,1000)
y1=[cosh(xi) for xi in x1]
plt.plot(x1,y1)
plt.title('Grafico de cosh(x)',fontsize=14)
plt.xlabel('x',fontsize=12)
plt.ylabel('cosh(x)',fontsize=12)
plt.show()

# Estimando o valor da integral usando a soma de Riemann das barras:
S = 0
for xi in x:
    S = S + cosh(xi)*0.02 
    
print('Soma das 500 barras =', round(S,5))

S1= 0
for xi in x1:
    S1 = S1 + cosh(xi)*0.01
print('Soma das 1000 barras = ', round(S1,5))
