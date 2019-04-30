class Ponto:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y

    def distancia_pontos(self, alvo):
        """ Retorna a distância entre dois pontos """
        dx = (self.x - alvo.x)
        dy = (self.y - alvo.y)
        return ((dx ** 2) + (dy ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

p = Ponto(3,4)
q = Ponto(8,16)
r = p.distancia_pontos(q)
print('a distância entre os pontos', str(p), 'e', str(q), 'é', r)
