import matplotlib.pyplot as plt
import numpy as np

# Primeira etapa -> MRU por 5 km:
d0 = 0 # em km
v0 = 12 # em km/h
t1 = np.arange(0,25,0.01) # em min
d1 = [d0+(v0/60)*t for t in t1] # em km

# Segunda etapa -> MUV por 200 m:
v1 = 15 # em km/h
delta_d = 0.2 # em km
a = (v1**2-v0**2)/(2*delta_d) # em km/(h**2)
delta_t = round(60*(v1-v0)/a,2) # em min
t2 = np.arange(25,25+delta_t,0.01) # em min
d2 = [5+(v0/60)*(t-25)+(a/7200)*(t-25)**2 for t in t2] # em km

# Terceira etapa -> MRU por 2 km:
dfinal = 7.2 # em km
delta_t1 = 60*(dfinal-5.2)/v1 # em min
t3 = np.arange(25+delta_t,25+delta_t+delta_t1,0.01) # em min
d3 = [5.2+(v1/60)*(t-(25+delta_t)) for t in t3]

# Plotando o gráfico:
plt.plot(t1,d1,'b')
plt.plot(t2,d2,'r')
plt.plot(t3,d3,'g')
plt.title('Distancia x Tempo',fontsize=14)
plt.xlabel('Tempo (min)',fontsize=12)
plt.ylabel('Distancia (km)',fontsize=12)
plt.show()

# Tempo para chegar em 7 km:
d = 7 # em km
t = (25+delta_t)+(d-5.2)/(v1/60) # em min
print('O tempo total para chegar em 7 km foi de', t, 'min.')
