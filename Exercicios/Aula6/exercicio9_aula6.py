import turtle

def polygon(t,length,n):
    for i in range(n):
        t.forward(length)
        t.right(360/n)
    t.penup()
    t.forward(150)
    t.pendown()

jn = turtle.Screen()
joana = turtle.Turtle()
polygon(joana,80,3)
polygon(joana,80,4)
polygon(joana,80,6)
jn.mainloop()
