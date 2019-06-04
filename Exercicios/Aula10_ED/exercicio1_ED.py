import matplotlib.pyplot as plt

d0 = 0
v = 12 #em km/h
t = [i for i in range(0,26)] #em min
d = [d0+v/60*ti for ti in t]

plt.plot(t,d)
plt.title('Distancia x Tempo',fontsize=14)
plt.xlabel('Tempo (min)',fontsize=12)
plt.ylabel('Distancia (km)',fontsize=12)
plt.show()

for i in range(0,len(d)):
    print('Com', i, 'min o maratonista havia percorrido', round(d[i],2), 'km')
