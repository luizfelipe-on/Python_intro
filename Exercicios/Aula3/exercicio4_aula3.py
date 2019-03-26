# Sabe-se que 1 milha = 1610 m, logo a função que converte de milhas para metros é:
def m(mi):
    m = mi*1610
    print(mi, 'milhas valem', round(m,3), 'metros')

m(4)

# Quanto à função que converte metros em milhas:
def mi(m):
    mi = m/float(1610) # usei o 'float' para que os resultados da divisão não fossem sempre números inteiros
    return mi

m = 3220
z1 = mi(m)
print(m, 'metros valem', round(z1,3), 'milhas')

# Como 1 h = 3600 s, a função que converte de horas para segundos é:
def s(h):
    s = h*3600
    print(h, 'horas valem', s, 'segundos')

s(3)

# Quanto à função que converte segundos em horas:
def h(s):
    h = s/float(3600)
    return h

s = 18000
z2 = h(s)
print(s, 'segundos valem', round(z2,3), 'horas')

# Podemos resolver o exercício 1 da aula 1 usando as funções acima. 
# Definamos a fórmula da velocidade em função do deslocamento e do tempo: 
def v(d,t):
    v = d/float(t)
    return v

# Como 10 km = 10*1000 m, 43.5 min = 43.5*60 s:
vmed = v(mi(10*1000),h(43.5*60))

# Então:
print('a velocidade média é de', round(vmed,3), 'milhas/h')

# Caso a pessoa leve 30 min para percorrer 4 milhas



