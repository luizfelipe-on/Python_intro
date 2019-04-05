import turtle

# Para que o programa solicite ao usuário as cores de fundo e da tartaruga, 
# e ainda a largura da caneta, pode-se usar a função 'input':
cor_fundo = input('a cor de fundo desejada é: ')          
cor_tartaruga = input('a cor da tartaruga desejada é: ')  
largura_caneta = input('a largura da caneta desejada é: ') 

# Abertura da janela de cor igual à cor_fundo:
jn = turtle.Screen()      
jn.bgcolor(cor_fundo)

# Criação da tartaruga, estabelecendo sua cor = cor_tartaruga
# e a largura da caneta = largura_caneta:
joana = turtle.Turtle()   
joana.color(cor_tartaruga) 
joana.pensize(largura_caneta)

# Fazendo com que a tartaruga se movimente:
joana.forward(50)          
joana.left(90)             
joana.forward(30)          

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()             
