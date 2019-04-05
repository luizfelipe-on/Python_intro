import turtle

# Alterei a função de 'square' para 'polygon' porque desejo que ela seja capaz de
# gerar diferentes figuras geométricas, não apenas quadrados. Para tal, acrescentei
# o parâmetro 'n', que nada mais é do que o número de lados do polígono, e agora o
# ângulo de desvio é de (360/n) graus:
def polygon(t,length,n):
    for i in range(n):
        t.forward(length)
        t.right(360/n)
    t.penup()
    t.forward(150)
    t.pendown()

# Abertura da janela e criação da tartaruga:
jn = turtle.Screen()
joana = turtle.Turtle()

# Para criar um triângulo, um quadrado e um hexágono de lado = 80 unidades, 
# respectivamente:
polygon(joana,80,3)
polygon(joana,80,4)
polygon(joana,80,6)

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()
