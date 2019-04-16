import turtle
import math

# Para obter uma flor de oito pétalas, podemos usar as funções 'polygon' e 'arc' do
# exercício 12. Já para criar o talo e a folha, precisamos criar novas funções:

def polygon(t,n,length,angle):        
    for j in range(8):
        for i in range(n):
            t.forward(length)
            t.left(angle)
        t.left(135)

def arc(t,r):
    n = 100
    circumference = 2*math.pi*r
    arc_length = 0.25*circumference
    step_length = arc_length/n
    step_angle = float(90)/n
    polygon(t,n,step_length,step_angle)
    
def leaf(t,r,theta):
    
    """ Função que possibilita que talo e folha sejam criados: """
    
    t.forward(r)
    t.left(theta)
    t.forward(r/2)
    t.right(2*theta)
    t.forward(r/2)
    t.left(theta)
    theta_rad = math.degrees(theta)
    cosine = math.cos(theta_rad)
    t.backward(r*cosine)
    t.forward(r*(1+cosine))

def flower(t,r,theta):
    
    """ Função que cria a flor de oito pétalas com talo e folha: """
    
    arc(t,r)
    t.penup()
    t.forward(0.7*r)
    t.pendown()
    t.right(90)
    leaf(t,r/2,theta)

# Abrindo a janela, criando a tartaruga e aumentando a velocidade da caneta: 
jn = turtle.Screen()
joana = turtle.Turtle()
joana.speed(10)

# Para obter uma flor composta por arcos de r = 100 unidades:
flower(joana,100,60)

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()
