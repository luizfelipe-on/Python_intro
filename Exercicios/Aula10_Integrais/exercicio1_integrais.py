import math
import numpy as np
import matplotlib.pyplot as plt

# 1) Colocando a curva à direita das barras:
x=np.linspace(0,10,100)
y=[math.exp(-xi) for xi in x]
plt.bar(x,y,color="red",align="edge",width=0.1)

x1=[i/100. for i in range(0,1000)]
y1=[math.exp(0.1-xi) for xi in x1]
plt.plot(x1,y1)
plt.title('Curva de exp(-x) a direita das barras',fontsize=14)
plt.xlabel('x',fontsize=12)
plt.ylabel('exp(-x)',fontsize=12)
plt.show()

# 1.1) Estimativa da integral pela direita:
Sd = 0
for xi in x1:
    Sd = Sd + math.exp(0.1-xi) * 0.01
print('Estimativa da integral pela direita é:', Sd)

# 2) Colocando a curva à esquerda das barras:
x=np.linspace(0,10,100)
y=[math.exp(-xi) for xi in x]
plt.bar(x,y,color="red",align="edge",width=0.1)

x1=[i/100. for i in range(0,1000)]
y1=[math.exp(-xi) for xi in x1]
plt.plot(x1,y1)
plt.title('Curva de exp(-x) a esquerda das barras',fontsize=14)
plt.xlabel('x',fontsize=12)
plt.ylabel('exp(-x)',fontsize=12)
plt.show()

# 2.1) Estimativa da integral pela esquerda:
Se = 0
for xi in x1:
    Se = Se + math.exp(-xi) * 0.01
print('Estimativa da integral pela esquerda é:', Se)
