import turtle
import math

# Definição da função 'polygon':
def polygon(t,length,n):
    for i in range(n):
        t.forward(length)
        t.right(360/n)

# Definição da função 'circle', que usa 'polygon', para n = 100:
def circle(t,r):
    circumference = 2*math.pi*r
    n = 100
    length = circumference/n  
    polygon(t,length,n)

# Abertura da janela e criação da tartaruga: 
jn = turtle.Screen()
joana = turtle.Turtle()

# Para obter círculos com r = 80 unidades:
circle(joana,80)

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()
