import turtle

# Para que o programa solicite ao usuário a cor de fundo desejada, 
# pode-se usar a função 'input':
cor_fundo = input('a cor de fundo desejada é: ')        
     
jn = turtle.Screen()      
jn.bgcolor(cor_fundo)

joana = turtle.Turtle()    

joana.forward(50)          
joana.left(90)             
joana.forward(30)          

jn.mainloop()             
