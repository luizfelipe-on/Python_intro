import turtle

# Neste caso, o lado do quadrado terá um número de unidades equivalente a 'length'. 
# Para criar distintos quadrados separados uns dos outros, usei 'penup' e 'pendown':
def square(t,length):
    for i in range(4):
        t.forward(length)
        t.right(90)
    t.penup()
    t.forward(200)
    t.pendown()
 
# Abertura da janela e criação da tartaruga: 
jn = turtle.Screen()
joana = turtle.Turtle()

# Para criar quadrados com lados = 40, 80 e 120 unidades, respectivamente:
square(joana,40)
square(joana,80)
square(joana,120)

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()
