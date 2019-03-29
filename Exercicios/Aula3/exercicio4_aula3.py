# Sabe-se que 1 milha = 1610 m, logo a função que converte de milhas para metros é:
def m(mi):
    m = mi*1610
    return m

print('2 milhas valem', round(m(2),3), 'metros')
print('5 milhas valem', round(m(5),3), 'metros')

# Quanto à função que converte metros em milhas:
def mi(m):
    mi = m/float(1610) # usei o 'float' para que os resultados da divisão não fossem sempre números inteiros
    return mi

print('3220 metros valem', round(mi(3220),3), 'milhas')
print('8050 metros valem', round(mi(8050),3), 'milhas')

# Como 1 h = 3600 s, a função que converte de horas para segundos é:
def s(h):
    s = h*3600
    return s

print('3 horas valem', round(s(3),3), 'segundos')
print('4 horas valem', round(s(4),3), 'segundos')

# Quanto à função que converte segundos em horas:
def h(s):
    h = s/float(3600)
    return h

print('10800 segundos valem', round(h(10800),3), 'horas')
print('14400 segundos valem', round(h(14400),3), 'horas')

# Podemos resolver o exercício 1 da aula 1 usando as funções acima. 
# Vamos definir a fórmula da velocidade em função do deslocamento e do tempo: 
def v(d,t):
    v = d/float(t)
    return v

# Como 10 km = 10*1000 m, 43.5 min = 43.5*60 s:
vmed = v(mi(10*1000),h(43.5*60))

# Então:
print('a velocidade média é de aproximadamente', round(vmed,3), 'milhas/h')

# Caso a pessoa leve 30 min para percorrer 4 milhas e deseje-se a velocidade em km/h:
# usar a função m(mi) que converte de milhas para metros e então dividir o valor por mil para passar para km;
# multiplicar 30 por 60 para conseguir o tempo em segundos, usando em seguida a função h(s) que converte de segundos para horas;
# usar a função v(d,t) que dá a velocidade média em função do deslocamento e do tempo.
vmed = v(m(4)*10**(-3),h(30*60))

# Então:
print('a velocidade média é de aproximadamente', round(vmed,3), 'km/h')
