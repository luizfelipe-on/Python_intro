# EXERCÍCIO 6

# A partir da equação de Torricelli, pode-se obter a velocidade final do objeto usando-se apenas a altura de queda.
# Assumindo que o objeto inicialmente estava em repouso e sabendo que ele caiu de 3 metros:

h = 3 # altura em metros
vo = 0 # velocidade inicial (repouso)
g = 9.8 # aceleração gravitacional em m/(s**2)
v = (vo**2+2*g*h)**0.5
print('a velocidade final do objeto é de:', v, 'm/s')

# O tempo que o objeto leva para cair, por sua vez, pode ser obtido a partir de:
t = (v-vo)/g
print('o tempo que o objeto demora para cair é de:', t, 'segundos')

