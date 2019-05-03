class Ponto:
    """ Cria um Ponto com coordenadas x, y """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

class Circulo:
    """ Cria um Círculo com raio e centro """

    def __init__(self, raio=0, centro=Ponto(0,0)):
        self.raio = raio
        self.centro = centro

    def __str__(self):
        return "({0}, {1})".format(self.raio, self.centro)

cen = Ponto()
cen.x = int(input('coordenada x do centro do círculo: '))
cen.y = int(input('coordenada y do centro do círculo: '))

cir = Circulo()
cir.raio = int(input('raio desejado do círculo: '))
cir.centro = cen

p = Ponto()
p.x = int(input('coordenada x do ponto: '))
p.y = int(input('coordenada y do ponto: '))

def ponto_circulo(q,r):
    if cen.x - r <= q.x <= cen.x + r and cen.y - r <= q.y <= cen.y + r:
        print('ponto', str(q), 'está dentro do círculo')
    else: 
        print('ponto', str(q), 'não está dentro do círculo')

ponto_circulo(p,cir.raio)

 
