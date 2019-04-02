import turtle

# Para que o programa solicite ao usuário as cores de fundo e da tartaruga, 
# e ainda a largura da caneta, pode-se usar a função 'input':
cor_fundo = input('a cor de fundo desejada é: ')          
cor_tartaruga = input('a cor da tartaruga desejada é: ')  
largura_caneta = input('a largura da caneta desejada é: ') 

jn = turtle.Screen()      
jn.bgcolor(cor_fundo)

joana = turtle.Turtle()   
joana.color(cor_tartaruga) 
joana.pensize(largura_caneta)

joana.forward(50)          
joana.left(90)             
joana.forward(30)          

jn.mainloop()             
