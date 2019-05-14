# Importing the modules:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the datafile and saving it in the variable 'ds':
ds = pd.read_csv('DoubleMuRun2011A.csv')

# Calculating the invariant mass of the first five pair of muons:
invariant_mass = np.sqrt(2*ds.pt1*ds.pt2*(np.cosh(ds.eta1-ds.eta2)-np.cos(ds.phi1-ds.phi2)))

# Definindo qual pico será ajustado:
ajuste = int(input('Qual pico você quer ajustar? Digite 1 para gamma ou 2 para bóson Z '))

if ajuste == 1:

    print('O histograma abaixo revela o pico de gamma:')
    
    lowerlimit = 9.25
    upperlimit = 9.65

# Let's select the invariant mass values that are inside the limitations.
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

# Let's create a histogram of the selected values.
    histogram = plt.hist(limitedmasses, bins=300, range=(lowerlimit,upperlimit))
    plt.xlabel('Invariant mass [in units GeV]')
    plt.ylabel('Number of events')
    plt.title('The Gaussian fit \n')
    plt.show()

# In y-axis the number of the events per each bin (can be got from the variable histogram).
# In x-axis the centers of the bins.
    y = histogram[0]
    x = 0.5*(histogram[1][0:-1] + histogram[1][1:])
# print('center of the bins =', x)
# print('number of events per bin =', y)

# Let's define a function that describes Gauss function distribution for the fit.
    def gauss_function(M, h, Mo, sigma):
        return h*np.exp(-(M-Mo)**2/(2*sigma**2))
    
    print('Uma curva gaussiana ajusta bem este histograma caso o usuário entre com valores adequados de h, Mo e sigma.')
    print('h representa a altura do pico da distribuição, Mo a massa correspondente a esta altura, e sigma o desvio padrão.')
    
# Initial values for the optimization in the following order:
    h = float(input('valor desejado da altura h: '))
    Mo = float(input('valor desejado da massa invariante Mo: '))
    sigma = float(input('valor desejado do desvio padrão: '))
    initials = [h, Mo, sigma]

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

    plt.hist(limitedmasses, bins=300, range=(lowerlimit,upperlimit))
    plt.plot(x, gauss_function(x, *best), 'r-', label='height = {}, Mo = {}'.format(best[0], best[1]))
    plt.xlabel('Invariant mass [in units GeV]')
    plt.ylabel('Number of events')
    plt.title('The Gaussian fit \n')
    plt.legend()
    plt.show()

if ajuste == 2:
    
    print('O histograma abaixo revela o pico do bóson Z:')
    
    lowerlimit = 70
    upperlimit = 110

# Let's select the invariant mass values that are inside the limitations.
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

# Let's create a histogram of the selected values.
    histogram = plt.hist(limitedmasses, bins=100, range=(lowerlimit,upperlimit))
    plt.xlabel('Invariant mass [in units GeV]')
    plt.ylabel('Number of events')
    plt.title('The Gaussian fit \n')
    plt.show()

# In y-axis the number of the events per each bin (can be got from the variable histogram).
# In x-axis the centers of the bins.
    y = histogram[0]
    x = 0.5*(histogram[1][0:-1] + histogram[1][1:])
# print('center of the bins =', x)
# print('number of events per bin =', y)

# Let's define a function that describes Breit-Wigner distribution for the fit.
# E is the energy, FWHM is the decay width, Mo the maximum of the distribution
# and a, b and A different parameters that are used for noticing the effect of
# the background events for the fit.
    def breitwigner(E, FWHM, Mo, a, b, A):
        return a*E+b+A*((2*np.sqrt(2)*Mo*FWHM*np.sqrt(Mo**2*(Mo**2+FWHM**2)))/(np.pi*np.sqrt(Mo**2+np.sqrt(Mo**2*(Mo**2+FWHM**2)))) )/((E**2-Mo**2)**2+Mo**2*FWHM**2)

    print('Uma curva Breit-Wigner ajusta bem este histograma caso o usuário entre com valores adequados de FWHM, Mo, a, b, A.')
    print('FWHM representa a largura à meia-altura, Mo a massa correspondente a esta FWHM.')
    print('a e b representam, respectivamente, a inclinação e a interceção em y usadas para notar o efeito de background.')
    print('A representa a altura da distribuição Breit-Wigner.')

# Initial values for the optimization in the following order:
    FWHM = float(input('valor desejado da largura à meia-altura FWHM: '))
    Mo = float(input('valor desejado da massa invariante Mo: '))
    a = float(input('valor desejado da inclinação usada para notar o efeito de background a: '))
    b = float(input('valor desejado da interceção em y usada para notar o efeito de background b: '))
    A = float(input('valor desejado da altura da distribuição Breit-Wigner A: '))
    initials = [FWHM, Mo, a, b, A]

# Let's import the module that is used in the optimization, run the optimization
# and calculate the uncertainties of the optimized parameters.
    from scipy.optimize import curve_fit
    best, covariance = curve_fit(breitwigner, x, y, p0=initials, sigma=np.sqrt(y))
    error = np.sqrt(np.diag(covariance))

# Let's print the values and uncertainties that are got from the optimization.
    print("The values and the uncertainties from the optimization: \n")
    first = "The value of the decay width (FWHM) = {} +- {}".format(best[0], error[0])
    second = "The value of the maximum of the distribution (Mo) = {} +- {}".format(best[1], error[1])
    third = "a = {} +- {}".format(best[2], error[2])
    fourth = "b = {} +- {}".format(best[3], error[3])
    fifth = "A = {} +- {}".format(best[4], error[4])
    print(first)
    print(second)
    print(third)
    print(fourth)
    print(fifth)

    plt.hist(limitedmasses, bins=100, range=(lowerlimit,upperlimit))
    plt.plot(x, breitwigner(x, *best), 'r-', label='FWHM = {}, Mo = {}'.format(best[0], best[1]))
    plt.xlabel('Invariant mass [in units GeV]')
    plt.ylabel('Number of events')
    plt.title('The Breit-Wigner fit \n')
    plt.legend()
    plt.show()
