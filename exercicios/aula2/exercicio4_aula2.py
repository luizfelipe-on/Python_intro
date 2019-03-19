# O comprimento de onda do laser é:
lamda = 632.8 # em nanômetros (nm)

# A distância do anteparo à fenda é:
D = 1.98 # em metros (m)

# O espaçamento entre as fendas é:
d = 0.25 # em milímetros (mm)

# Convertendo lamda e d para metros, a distância entre dois máximos de interferência consecutivos é de:
delta_y = (lamda*(10**(-9))*D) / (d*(10**(-3)))
print('a distância entre dois máximos de interferência consecutivos é de', delta_y, 'metros')


