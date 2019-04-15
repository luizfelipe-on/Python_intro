import turtle

# Criação da função 'draw_bar', que desenha barras. Vamos utilizá-la para fazer o histograma:

def draw_bar(t,frequencies):
    
    """ Enquanto 't' é uma turtle, 'frequencies' tem de ser uma lista para funcionar: """

    if type(frequencies) == list:
        print(frequencies,'é uma lista')
        binning = input('bin desejado: ')
        for height in frequencies:
            t.begin_fill()           
            t.left(90)
            t.forward(height)
            t.write("  " + str(height))
            t.right(90)
            t.forward(int(binning))
            t.right(90)
            t.forward(height)
            t.left(90)
            t.end_fill()     
    else:
        print('Erro!',frequencies,'não é uma lista')

# Abrindo a janela e dando a ela uma cor de fundo:
jn = turtle.Screen()         
jn.bgcolor("lightgreen")

# Criando uma tartaruga, estabelecendo suas cores e a largura da caneta:
joana = turtle.Turtle()   
color1 = input('cor do contorno desejada: ')    
color2 = input('cor de preenchimento desejada: ')    
joana.color(color1,color2)
joana.pensize(3)

# Solicitação da lista de frequências e execução da função:
xs = [48,117,200,240,160,260,220]
draw_bar(joana,xs)

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()
