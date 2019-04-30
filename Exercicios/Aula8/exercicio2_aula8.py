class Ponto:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y
    
    def reflexao_x(self):
        """ Retorna a reflexão do ponto no eixo-x """
        rx = -1*self.x
        ry = 1*self.y
        return rx,ry

p = Ponto(3,4)
r = p.reflexao_x()
print('a reflexão do ponto sobre o eixo-x é',r)
