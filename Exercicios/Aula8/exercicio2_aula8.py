class Ponto:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y
    
    def reflexao_x(self):
        """ Retorna o reflexo do ponto sobre o eixo-x """
        rx = self.x
        ry = -self.y
        return Ponto(rx,ry)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

p = Ponto(3,5)
ref = p.reflexao_x()
print('o reflexo do ponto', str(p), 'sobre o eixo-x é', ref)
