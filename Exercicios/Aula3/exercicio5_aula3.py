import math

# Função para o exercício 5 da aula 1:
def IMC(M,H):
    IMC = M/H**2
    print('o IMC é de aproximadamente', round(IMC,2))

# No meu caso: 
IMC(69,1.79)

# No caso do bebê:
IMC(11,0.7)

# Função para o exercício 2 da aula 2:
def V(R):
    V = (4*math.pi*R**3)/3
    print('o volume da esfera é de cerca de', round(V,2))
    
V(5)

# Função para o exercício 4 da aula 2:

# Na definição da função, há de se considerar que o comprimento de onda é dado em nanômetros e o espaçamento em milímetros,
# então para se obter a resposta em metros: 
def delta_y(lamda,D,d):
    delta_y = lamda*10**(-9)*D/(d*10**(-3))
    print('a distância entre dois máximos consecutivos de interferência é de aproximadamente', round(delta_y,2), 'metros')
     
delta_y(632.8,1.98,0.25)

