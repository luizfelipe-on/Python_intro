import turtle

# Criação da função 'draw_bar', que desenha barras, utilizando 'try' e 'except'.
# Caso o argumento 'frequencies' não seja uma lista, a exceção é acionada.

def draw_bar(t,frequencies):
    try:
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
    except:
        return 'Um erro ocorreu, o histograma não pôde ser plotado'

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
xs = 220
draw_bar(joana,xs)

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()
