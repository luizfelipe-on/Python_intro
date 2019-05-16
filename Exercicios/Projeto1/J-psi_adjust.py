import math

# Importing the modules:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the datafile and saving it in the variable 'ds':
ds = pd.read_csv('DoubleMuRun2011A.csv')

# Calculating the invariant mass of all pairs of muons:
invariant_mass = np.sqrt(2*ds.pt1*ds.pt2*(np.cosh(ds.eta1-ds.eta2)-np.cos(ds.phi1-ds.phi2)))

# J/psi peak histogram:
print('Histograma abaixo revela o pico de J/psi:')
lowerlimit = 2.8 
upperlimit = 3.4
limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]
plt.hist(limitedmasses, bins=100, range=(lowerlimit,upperlimit))
plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of events')
plt.title('J/psi peak histogram \n')
plt.show()

# In y-axis, the number of events per bin, which can be got from the variable 'histogram'.
# In x-axis, the centers of the bins.
histogram = plt.hist(limitedmasses, bins=100, range=(lowerlimit,upperlimit))
y = histogram[0]
x = 0.5*(histogram[1][0:-1] + histogram[1][1:])

# Defining a function that describes Crystalball distribution for the fit:
def crystalball_function(M, alpha, n, Mo, sigma):
    if (M-Mo)/sigma > -alpha: 
        return sigma*(n*exp(-(alpha**2)/2)/(abs(alpha)*(n-1)) + math.sqrt(math.pi/2)*()) ..... ** (-1)
    if (M-Mo)/sigma <= -alpha:
        return
          
# Initial values for the optimization in the following order:
alpha = float(input('alpha: '))
n = float(input('n: '))
Mo = float(input('Mo: '))
sigma = float(input('sigma: '))
print("")
initials = [alpha, n, Mo, sigma]

# Importing the module that is used in the optimization, running the optimization
# and calculating the uncertainties of the optimized parameters:
from scipy.optimize import curve_fit
best, covariance = curve_fit(crystalball_function, x, y, p0=initials)
error = np.sqrt(np.diag(covariance))

# Printing the values and uncertainties gotten from the optimization:
print("Valores e Incertezas da Optimização:")
first = "Valor optimizado de alpha = {} +- {}".format(best[0], error[0])
second = "Valor optimizado de n = {} +- {}".format(best[1], error[1])
third = "Valor optimizado de Mo = {} +- {}".format(best[2], error[2])
fourth = "Valor optimizado de sigma = {} +- {}".format(best[3], error[3])
print(first)
print(second)
print(third)
print(fourth)

# Plotting the histogram with the Gaussian adjust:
plt.hist(limitedmasses, bins=100, range=(lowerlimit,upperlimit))
plt.plot(x, crystalball_function(x, *best), 'b-', label='Mo = {}'.format(best[2]))
plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of events')
plt.title('The Crystalball fit \n')
plt.legend()
plt.show()
