class Matriz:

    def __init__(self):
        self.matrix = {(0,3): 1, (2,1): 2, (4,3): 3}

    def teste(self, x, y):
        return self.matrix.get((x,y),0)

    def __str__(self):
        return str(self.matrix)

m = Matriz()
m1 = m.teste(2,0)
m2 = m.teste(2,1)
print(m1,m2)
