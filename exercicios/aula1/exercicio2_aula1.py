# EXERCÍCIO 2

# Sabe-se que as velocidades da luz e do som (em m/s) são, respectivamente:
v_luz = 3*10**8
v_som = 343

# Como ambos percorrem a mesma distância d, com o som levando 3 segundos a mais (t_som = t_luz + 3), então:
# d = 3*(10**8)*t_luz = 343*(t_luz+3)
t_luz = 1029/299999657

# Logo a distãncia d em que os fogos foram lançados é de:
d = 3*(10**8)*t_luz
print('a distância d em que os fogos foram lançados é de ', d, ' metros')
