import turtle
import math

# Definição da função 'polygon':
def polygon(t,length,n):
    for i in range(n):
        t.forward(length)
        t.left(360/n)
    t.penup()
    t.forward(length+200)
    t.pendown()

# Definição da função 'circle', que usa 'polygon', para n = 100:
def circle(t,r):
    n = 100
    circumference = 2*math.pi*r
    length = circumference/n
    polygon(t,length,n)

# Abertura da janela e criação da tartaruga: 
jn = turtle.Screen()
joana = turtle.Turtle()

# Para obter círculos com r = 30, 50 e 80 unidades, respectivamente:
circle(joana,30)
circle(joana,50)
circle(joana,80)

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()
