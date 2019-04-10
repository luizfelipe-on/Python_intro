import turtle
import math

# Para criar um polígono formado por n triângulos isósceles, definimos a seguinte função: 

def polygon(t,l,n):

    """ Estabelecemos que cada triângulo possui dois lados l e um terceiro L. Estabelecemos 
    também que o ângulo que os lados l fazem entre si é a, e o que fazem com L é b, de forma 
    que theta é o ângulo suplementar a b. Sendo assim, obtém-se que: """

    a = 360/n
    b = (180-a)/2
    theta = 180-b
    B = math.radians(b)
    L = 2*l*math.cos(B)

    """ Para gerar os n triângulos do polígono, pode-se usar o seguinte laço 'for': """

    for i in range(n):
        t.forward(l)
        t.left(theta)
        t.forward(L)
        t.left(theta)
        t.forward(l)
        t.left(180)

    """ Para que diferentes polígonos espaçados possam ser formados: """

    t.penup()
    t.forward(l+150)
    t.pendown()

# Abertura da janela e criação da tartaruga:
jn = turtle.Screen()
joana = turtle.Turtle()

# Criação de polígonos com l = 100 unidades formados por 5, 6 e 7 triângulos isósceles, 
# respectivamente:
polygon(joana,100,5)
polygon(joana,100,6)
polygon(joana,100,7)

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()
