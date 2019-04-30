class Ponto:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y
    
    def parametros_reta(self,alvo):
        """ Retorna os coeficientes a, b da equação da reta y = ax + b """
        a = float((self.y - alvo.y))/(self.x - alvo.x)
        b = float(self.y) - (a*self.x)
        return a,b

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

p = Ponto(4,11)
q = Ponto(6,15)
par = p.parametros_reta(q)
print('os coeficientes (a, b) da equação da reta que passa pelos pontos', str(p), 'e', str(q), 'são', par)
