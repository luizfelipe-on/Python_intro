# Importing the modules:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the datafile and saving it in the variable 'ds':
ds = pd.read_csv('DoubleMuRun2011A.csv')

# Opening the datafile:
print('Datafile is:\n', ds)

# Estimating the number of collisions:
print('The number of collisions is:', len(ds))

# Printing the first five lines of the datafile:
print('Information of the first five lines of the datafile:\n', ds.head())

# Calculating the invariant mass of the first five pair of muons:
invariant_mass = np.sqrt(2*ds.pt1*ds.pt2*(np.cosh(ds.eta1-ds.eta2)-np.cos(ds.phi1-ds.phi2)))
print('The invariant mass values of the first five pair of muons are (in units GeV):')
print(invariant_mass[0:5])

# Rest of the code is for checking if the values are correct using line 5 as reference. We don't have to change that:
if 14.31 <= invariant_mass.values[4] <= 14.32:
    print('Invariant mass values are correct!')
else:
    print('Calculated values are not yet correct. Please check the calculation one more time.')
print('Remember: don´t change the name of the variable invariant_mass.')

# Creating the histogram:
plt.hist(invariant_mass, bins = 10, range = (80,100))
plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of events')
plt.title('Histogram of invariant mass values of two muons. \n')
plt.show()

# Let's limit the fit near to the peak of the histogram.
lowerlimit = 70
upperlimit = 110

# Let's select the invariant mass values that are inside the limitations.
limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

# Let's create a histogram of the selected values.
histogram = plt.hist(limitedmasses, bins=100, range=(lowerlimit,upperlimit))

# In y-axis the number of the events per each bin (can be got from the variable histogram).
# In x-axis the centers of the bins.
y = histogram[0]
x = 0.5*(histogram[1][0:-1] + histogram[1][1:])
# print('center of the bins =', x)
# print('number of events per bin =', y)

# Let's define a function that describes Breit-Wigner distribution for the fit.
# E is the energy, gamma is the decay width, M the maximum of the distribution
# and a, b and A different parameters that are used for noticing the effect of
# the background events for the fit.
def breitwigner(E, gamma, M, a, b, A):
    return a*E+b+A*((2*np.sqrt(2)*M*gamma*np.sqrt(M**2*(M**2+gamma**2)))/(np.pi*np.sqrt(M**2+np.sqrt(M**2*(M**2+gamma**2)))) )/((E**2-M**2)**2+M**2*gamma**2)

# Initial values for the optimization in the following order:
# gamma (the full width at half maximum (FWHM) of the distribution);
# M (the maximum of the distribution);
# a (the slope that is used for noticing the effect of the background);
# b (the y intercept that is used for noticing the effect of the background);
# A (the "height" of the Breit-Wigner distribution).
initials = [4.5, 91, -2, 200, 13000]

# Let's import the module that is used in the optimization, run the optimization
# and calculate the uncertainties of the optimized parameters.
from scipy.optimize import curve_fit
best, covariance = curve_fit(breitwigner, x, y, p0=initials, sigma=np.sqrt(y))
error = np.sqrt(np.diag(covariance))

# Let's print the values and uncertainties that are got from the optimization.
print("The values and the uncertainties from the optimization: \n")
first = "The value of the decay width (gamma) = {} +- {}".format(best[0], error[0])
second = "The value of the maximum of the distribution (M) = {} +- {}".format(best[1], error[1])
third = "a = {} +- {}".format(best[2], error[2])
fourth = "b = {} +- {}".format(best[3], error[3])
fifth = "A = {} +- {}".format(best[4], error[4])
print(first)
print(second)
print(third)
print(fourth)
print(fifth)

plt.plot(x, breitwigner(x, *best), 'r-', label='gamma = {}, M = {}'.format(best[0], best[1]))
plt.xlabel('Invariant mass [in units GeV]')
plt.ylabel('Number of events')
plt.title('The Breit-Wigner fit \n')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ds = pd.read_csv('DoubleMuRun2011A.csv')
invariant_mass_1 = ds['M']

# Let's calculate the logarithms of the masses and weights.
no_bins = 500
inv_mass_log = np.log10(invariant_mass_1)
weights = []
for a in invariant_mass_1:
    weights.append(no_bins/np.log(10)/a)

# Let's plot the weighted histogram.
plt.hist(inv_mass_log, no_bins, range=(-0.5,2.5), weights=weights, lw=0, color="darkgrey")
plt.yscale('log')

# Naming the labels and the title.
plt.xlabel('log10(invariant mass) [log10(GeV)]')
plt.ylabel('Number of the events')
plt.title('The histogram of the invariant masses of two muons \n')
plt.show()
