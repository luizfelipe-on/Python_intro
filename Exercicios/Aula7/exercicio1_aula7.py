import turtle

def draw_bar(t,frequencies,binning):

    """ Get turtle t to draw one bar, of height. """

    if type(frequencies) == list:
        print(frequencies,'é uma lista') 
        for height in frequencies:
            t.begin_fill()           
            t.left(90)
            t.forward(height)
            t.write("  "+ str(height))
            t.right(90)
            t.forward(binning)
            t.right(90)
            t.forward(height)
            t.left(90)
            t.end_fill()     
    else:
        print('Erro!',frequencies,'não é uma lista')        

wn = turtle.Screen()         
wn.bgcolor("lightgreen")

tess = turtle.Turtle()   
color1 = input('cor do contorno desejada é: ')    
color2 = input('cor de preenchimento desejada é: ')    
tess.color(color1,color2)
tess.pensize(3)

xs = [48,117,200,240,160,260,220]
draw_bar(tess,xs,50)

wn.mainloop()
