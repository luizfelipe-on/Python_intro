import turtle

# Abertura da janela e estabelecendo seu título:
jn = turtle.Screen()         
jn.title("Quatro Estrelas Verdes")

# Criando a tartaruga, estabelecendo sua cor como verde e a largura da caneta como 2:
estrela = turtle.Turtle()       
estrela.color("green")
estrela.pensize(2)

# Para criar 4 estrelas iguais lado a lado separadas por uma pequena distância,
# pode-se usar um laço 'for' dentro de outro: o interno para criar cada estrela,
# o externo para fazer com que o processo interno ocorra 4 vezes, com as estrelas
# ficando separadas umas das outras:
for j in range(4):
    for i in range(5):
        estrela.forward(80)            
        estrela.right(144)
    estrela.penup()
    estrela.forward(120)
    estrela.pendown()

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()
