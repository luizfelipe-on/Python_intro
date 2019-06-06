import matplotlib.pyplot as plt

# Dados do problema:
d0 = 0 # em km
dfinal = 5 # em km
v = 12 # em km/h

# O maratonista atinge os 5 km no seguinte tempo:
t1 = int(60*(dfinal-d0)/v) # em min

# Lista dos tempos entre 0 e t1 minutos divididos em intervalos de 1 min:
t = [i for i in range(0,t1+1)] # em min

# Então:
d = [d0+v/60*ti for ti in t]
print('A lista com as distâncias (em km) percorridas a cada minuto de 0 a', t1, 'min é:', d)
