import turtle
import math

# Definição da função 'polygon' adicionando 'angle' como argumento:
def polygon(t,n,length,angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)
    t.penup()
    t.forward(100)
    t.pendown()

# Definição da função 'arc', que usa 'polygon', para n = 100:
def arc(t,r,angle):  
    n = 100
    circumference = 2*math.pi*r
    arc_length = circumference*angle/360
    step_length = arc_length/n
    step_angle = float(angle)/n
    polygon(t,n,step_length,step_angle)

# Abertura da janela e criação da tartaruga: 
jn = turtle.Screen()
joana = turtle.Turtle()

# Para obter arcos com r = 40 unidades e ângulos = 90, 180, 270 e 360 graus, respectivamente:
arc(joana,40,90)
arc(joana,40,180)
arc(joana,40,270)
arc(joana,40,360)

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()
