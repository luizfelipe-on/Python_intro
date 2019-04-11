import turtle
import math

# Podemos obter uma flor de oito pétalas adaptando as funções 'polygon' e 'arc', que foram 
# criadas em exercícios anteriores. A flor corresponderá a um conjunto de arcos de comprimento 
# igual a 1/4 de circunferência:

def polygon(t,n,length,angle):
    
    """ Primeiramente colocamos o laço 'for' da antiga função 'polygon' dentro de um laço
    'for' de comprimento igual a oito . Além disso, cada vez que 1/4 de circunferência for 
     criado, a tartaruga deve virar 135 graus para a esquerda: """
    
    for j in range(8):
        for i in range(n):
            t.forward(length)
            t.left(angle)
        t.left(135)

def arc(t,r):
    
    """ A flor será obtida a partir de um conjunto de arcos que equivalem a 1/4 de
    circunferência, ou seja, arcos que subentendem ângulos de 90 graus: """
    
    n = 100
    circumference = 2*math.pi*r
    arc_length = 0.25*circumference
    step_length = arc_length/n
    step_angle = float(90)/n
    polygon(t,n,step_length,step_angle)

# Abertura da janela e criação da tartaruga: 
jn = turtle.Screen()
joana = turtle.Turtle()

# Para obter uma flor de oito pétalas composta por arcos de r = 100 unidades:
arc(joana,100)

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()
