import turtle

# Para que o programa solicite ao usuário as cores de fundo e da tartaruga, 
# e ainda a largura da caneta, pode-se usar a função 'input':
cor_fundo = input('a cor de fundo desejada é: ')          
cor_tartaruga = input('a cor da tartaruga desejada é: ')  
largura_caneta = input('a largura da caneta desejada é: ') 

# Abertura da janela com cor igual à cor_fundo:
jn = turtle.Screen()      
jn.bgcolor(cor_fundo)

# Criação da tartaruga, estabelecendo sua cor = cor_tartaruga, 
# a largura da caneta = largura_caneta, o formato de tartaruga  
# e velocidade = 2:
joana = turtle.Turtle()
joana.color(cor_tartaruga) 
joana.pensize(largura_caneta)
joana.shape('turtle') # faz com que a forma de tartaruga seja usada
joana.speed(2) # faz com que a velocidade 2 seja usada 

# Fazendo com que a tartaruga se movimente:
joana.forward(50)          
joana.left(90)             
joana.forward(30)          

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()    
