import turtle

# Criando um quadrado de lado = 80 unidades usando turtle:
def square(t):
    for i in range(4):
        t.forward(80)
        t.right(90)

jn = turtle.Screen()
joana = turtle.Turtle()
square(joana)
jn.mainloop()
