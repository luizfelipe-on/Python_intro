import turtle

# Para que o programa solicite ao usuário a cor de fundo desejada, 
# pode-se usar a função 'input':
cor_fundo = input('a cor de fundo desejada é: ')        
  
# Abertura da janela com cor igual à cor_fundo:
jn = turtle.Screen()      
jn.bgcolor(cor_fundo)

# Criação da tartaruga e fazendo ela se deslocar:
joana = turtle.Turtle()    
joana.forward(50)          
joana.left(90)             
joana.forward(30)          

# Para garantir que o programa só acabe quando eu fechar a janela:
jn.mainloop()     
