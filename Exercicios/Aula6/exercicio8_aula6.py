import turtle

# Neste caso, o lado do quadrado terá um número de unidades equivalente a 'length', 
# que é definido dentro da função 'square'. Como desejo criar diferentes quadrados
# separados uns dos outros, usei as funções 'penup' e 'pendown':
def square(t,length):
    for i in range(4):
        t.forward(length)
        t.right(90)
    t.penup()
    t.forward(200)
    t.pendown()

jn = turtle.Screen()
joana = turtle.Turtle()

# Para criar quadrados com lados = 40, 80 e 120, respectivamente:
square(joana,40)
square(joana,80)
square(joana,120)

jn.mainloop()
