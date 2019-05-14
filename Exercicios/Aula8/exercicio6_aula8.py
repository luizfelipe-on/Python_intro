import math

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
        
    def area(self):                                    
        """Retorna a área do círculo"""
        a = math.pi*((self.raio)**2)
        return a
    
    def ponto_circulo(self, p = Ponto()):
        d = ((p.x - self.centro.x)**2 + (p.y - self.centro.y)**2) ** 0.5
        if d <= self.raio:
            return "True"
        else:
            return "False"

    def __str__(self):
        return "({0}, {1})".format(self.raio, self.centro)

# Defining um círculo de raio = 50 e centro = (10,10):
circ = Circulo(50, Ponto(10, 10))

# Definindo os seguintes pontos p, q: 
p = Ponto(40,30)
q = Ponto(35,70)

# Verificando se os pontos p, q estão dentro do círculo:
print('Ponto', str(p), 'pertence ao círculo', str(circ), '?', circ.ponto_circulo(p))
print('Ponto', str(q), 'pertence ao círculo', str(circ), '?', circ.ponto_circulo(q))

