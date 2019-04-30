class Ponto:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y
    
    def inclinacao_origem(self):
        """ Retorna a inclinação da linha que une o ponto à origem """
        dx = self.x - 0
        dy = self.y - 0
        return float(dy)/dx

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

p = Ponto(4,10)
inc = p.inclinacao_origem()
print('a inclinação da linha que une o ponto', str(p), 'à origem é', inc)

# O programa não funciona quando tentamos calcular a inclinação do ponto (0,0). A resposta deveria ser 
# zero, mas como no método inclinacao_origem() haveria a divisão por zero, o Python retorna erro:
# p = Ponto(0,0)
# inc = p.inclinacao_origem()
# print('a inclinação da linha que une o ponto', str(p), 'à origem é', inc)
