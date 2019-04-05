import turtle

# Definindo uma função que crie um quadrado de lado = 80 unidades usando tartaruga:
def square(t):
    for i in range(4):
        t.forward(80)
        t.right(90)

# Abertura da janela e criação da tartaruga: 
jn = turtle.Screen()
joana = turtle.Turtle()

# Desenhando o quadrado:
square(joana)

# Para garantir que o programa só termine quando eu fechar a janela.
jn.mainloop()
