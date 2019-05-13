# Let's limit the fit near to the peak of the histogram.
lowerlimit = 9.25
upperlimit = 9.65

# Let's select the invariant mass values that are inside the limitations.
limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

# Let's create a histogram of the selected values.
histogram = plt.hist(limitedmasses, bins=300, range=(lowerlimit,upperlimit))

# In y-axis the number of the events per each bin (can be got from the variable histogram).
# In x-axis the centers of the bins.
y = histogram[0]
x = 0.5*(histogram[1][0:-1] + histogram[1][1:])
# print('center of the bins =', x)
# print('number of events per bin =', y)

# Let's define a function that describes Gauss function distribution for the fit.
def gauss_function(M, h, Mo, sigma):
    return h*np.exp(-(M-Mo)**2/(2*sigma**2))

# Initial values for the optimization in the following order:
# h (the height of the distribution for the invariant mass of gamma);
# Mo (the invariant mass expected for gamma);
# sigma (the standard deviation);
initials = [72, 9.45, 0.12]

# Let's import the module that is used in the optimization, run the optimization
# and calculate the uncertainties of the optimized parameters.
from scipy.optimize import curve_fit
best, covariance = curve_fit(gauss_function, x, y, p0=initials)
error = np.sqrt(np.diag(covariance))

# Let's print the values and uncertainties that are got from the optimization.
print("The values and the uncertainties from the optimization: \n")
first = "The value of the maximum height (h) = {} +- {}".format(best[0], error[0])
second = "The value of gamma invariant mass (Mo) = {} +- {}".format(best[1], error[1])
third = "sigma = {} +- {}".format(best[2], error[2])
print(first)
print(second)
print(third)

plt.plot(x, gauss_function(x, *best), 'r-', label='height = {}, Mo = {}'.format(best[0], best[1]))
plt.xlabel('Invariant mass [in units GeV]')
plt.ylabel('Number of events')
plt.title('The Gaussian fit \n')
plt.legend()
plt.show()
