import turtle

# Definição da função 'polygon':
def polygon(t,length,n):
    for i in range(n):
        t.forward(length)
        t.right(360/n)

# Abertura da janela e criação da tartaruga: 
jn = turtle.Screen()
joana = turtle.Turtle()

# Usando-se n = 360 e length = 1, 'polygon' cria um círculo:
polygon(joana,1,360)
