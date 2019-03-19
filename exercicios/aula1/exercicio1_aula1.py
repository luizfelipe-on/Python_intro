# A distância (em km) e o tempo (em min) são, respectivamente: 
d = 10 
t = 43.5

# Como 1 milha = 1.61 km e 1 h = 60 min, a velocidade média em milhas/h é:

vmed = (d/1.61)/(t/60)
print('a velocidade média é de', vmed, 'milhas/h')

# Sendo assim, o tempo médio por milha (em min/milha) é de:

tmed = (vmed**(-1))*60
print('o tempo médio é de', tmed, 'min/milha')
