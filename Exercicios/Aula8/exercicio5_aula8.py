class Ponto:
    """ Cria um Ponto com coordenadas x, y """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

class Retangulo:
    """ Cria um Retângulo com altura, largura e vértices """

    def __init__(self, largura=0, altura=0, canto=Ponto(0,0)):
        self.largura = largura
        self.altura = altura
        self.canto = canto

    def vertices(self):
        v1 = (self.canto.x, self.canto.y)
        v2 = (self.canto.x + self.largura, self.canto.y)
        v3 = (self.canto.x, self.canto.y + self.altura)
        v4 = (self.canto.x + self.largura, self.canto.y + self.altura) 
        return v1, v2, v3, v4

    def __str__(self):
        return "({0}, {1}, {2})".format(self.largura, self.altura, self.canto)

# Solicitação de um ponto qualquer ao usuário:
p = Ponto()
p.x = int(input('coordenada x do ponto: '))
p.y = int(input('coordenada y do ponto: '))

# Solicitação da largura e da altura do retângulo ao usuário, usando o ponto acima como o canto do retângulo:   
ret = Retangulo()
ret.largura = int(input('largura desejada do retângulo: '))
ret.altura = int(input('altura desejada do retângulo: '))
ret.canto = p

# Definição dos vértices do retângulo a partir do ponto e das dimensões do retângulo:
vert = ret.vertices() 
print('os vértices do retângulo são', vert)
