# Importando os pacotes necessários:
import math
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from astropy.io import fits
from astropy.table import Table

# Importando o arquivo CSV que contém os dados dos aglomerados da MW e o salvando na variável 'tab':
tab = pd.read_csv('asu.csv')

# Verificando o header completo de 'tab':
tab.head(3008)

# Obtendo os dados necessários para Table.txt, que são RA, Dec e distância somente dos aglomerados globulares:
for i in range(0,len(tab.map)):
    if tab.Type[i] == 'g':
        print(tab.MWSC[i],tab.RAJ2000[i],tab.DEJ2000[i],tab.d[i])
        
# Importando a tabela com os dados dos aglomerados globulares:
table1 = np.loadtxt('Table.txt',dtype={'names':('identification','right_ascension','declination','distance'),
                                       'formats':('i8','f8','f8','i8')}, unpack=True, delimiter=',')

identification = table1[0]
right_ascension = table1[1]
declination = table1[2]
distance = table1[3]

# Distribuição da distância dos aglomerados globulares ao centro da Via Láctea:
r = []
for i in range(0,len(identification)):
    r.append(distance[i])
        
plt.hist(r,bins=10,range=(0,50000))
plt.title('Distribuicao das Distancias dos Aglomerados Globulares',fontsize=14)
plt.xlabel('Distancia [pc]',fontsize=12)
plt.ylabel('Frequencia',fontsize=12)
plt.show()

# O histograma permite constatar que a maioria dos aglomerados estão próximos ao centro da galáxia.
# No entanto, o enunciado solicita que apenas os mais distantes sejam considerados no cálculo da
# distância média ao centro da MW, já que eles que se distribuem de forma esférica ao redor do centro.
# Sendo assim, faremos um corte em 10 kpc, ou seja, apenas aglomerados além desta distância serão 
# considerados nos próximos cálculos.

# Convertendo as coordenadas esféricas em cartesianas para os aglomerados além de 10 kpc:
x = []
y = []
z = []

for i in range(0,len(identification)):
    RA = math.pi/180*right_ascension[i] #ascensão reta convertida de graus para radianos
    Dec = math.pi/180*declination[i] #declinação convertida de graus para radianos
    d = distance[i]
    
    if d > 10000:
        x.append(d*np.sin(math.pi/2-Dec)*np.cos(RA))
        y.append(d*np.sin(math.pi/2-Dec)*np.sin(RA))
        z.append(d*np.cos(math.pi/2-Dec))
        
# Obtendo os valores médios das coordenadas cartesianas:
x_avg = np.mean(x)
y_avg = np.mean(y)
z_avg = np.mean(z)

# Calculando a distância média desdes aglomerados globulares ao centro da Via Láctea:
d_avg = (x_avg**2 + y_avg**2 + z_avg**2) ** 0.5
print('A distância média dos aglomerados globulares ao centro da Via Láctea é de aproximadamente', round(d_avg,3), 'pc')
