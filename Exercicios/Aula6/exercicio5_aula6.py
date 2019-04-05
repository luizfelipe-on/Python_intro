import turtle

# Abertura da janela e estabelecendo seu título:
jn = turtle.Screen()         
jn.title("Estrela Azul")

# Criando a tartaruga, estabelecendo sua cor como azul e a largura da caneta como 2:
estrela = turtle.Turtle()       
estrela.color("blue")
estrela.pensize(2)

# Como cada ponta de uma estrela de 5 pontas possui um ângulo interno de 36 graus,
# o ângulo de virada para a direita da tartaruga (aqui chamada 'estrela') tem de 
# ser (180 - 36) = 144 graus: 
for i in range(5):
    estrela.forward(80)            
    estrela.right(144)

# Para garantir que o programa só acabe quando eu fechar a janela:   
jn.mainloop()
