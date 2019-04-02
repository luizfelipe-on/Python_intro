import turtle

def square(t,length):
    for i in range(4):
        t.forward(length)
        t.right(90)
    t.penup()
    t.forward(200)
    t.pendown()

jn = turtle.Screen()
joana = turtle.Turtle()
square(joana,40)
square(joana,80)
square(joana,120)
jn.mainloop()
