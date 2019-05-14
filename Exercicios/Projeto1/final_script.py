# Importing the modules:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the datafile and saving it in the variable 'ds':
ds = pd.read_csv('DoubleMuRun2011A.csv')

# Calculating the invariant mass of all pairs of muons:
invariant_mass = np.sqrt(2*ds.pt1*ds.pt2*(np.cosh(ds.eta1-ds.eta2)-np.cos(ds.phi1-ds.phi2)))

# Defining whick peak will be adjusted:
ajuste = int(input('Qual pico você quer ajustar? Digite 1 para upsilon ou 2 para bóson Z '))

# If the peak of upsilon was chosen, the following histogram can be plotted:
if ajuste == 1:
    print('Histograma abaixo revela o pico de upsilon:')
    lowerlimit = 9.25 
    upperlimit = 9.65
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]
    plt.hist(limitedmasses, bins=300, range=(lowerlimit,upperlimit))
    plt.xlabel('Invariant mass [GeV]')
    plt.ylabel('Number of events')
    plt.title('The Gaussian fit \n')
    plt.show()

# In y-axis, the number of events per bin, which can be got from the variable 'histogram'.
# In x-axis, the centers of the bins.
    histogram = plt.hist(limitedmasses, bins=300, range=(lowerlimit,upperlimit))
    y = histogram[0]
    x = 0.5*(histogram[1][0:-1] + histogram[1][1:])
    # print('center of the bins =', x)
    # print('number of events per bin =', y)

# Defining a function that describes Gauss distribution for the fit:
    def gauss_function(M, h, Mo, sigma):
        return h*np.exp(-(M-Mo)**2/(2*sigma**2))
    
    print('Uma curva Gaussiana ajusta bem este histograma caso o usuário entre com valores adequados de h, Mo e sigma.')
    print('h representa um chute inicial da altura do pico da distribuição.')
    print('Mo representa um chute inicial da massa invariante correspondente a esta altura.')
    print ('sigma representa um chute inicial do desvio padrão da distribuição.')
    print('Dica: Em uma distribuição gaussiana, sigma ~ FWHM/2. \n')
          
# Initial values for the optimization in the following order:
    h = float(input('Valor inicial da altura máxima h: '))
    Mo = float(input('Valor inicial da massa invariante Mo: '))
    sigma = float(input('Valor inicial do desvio padrão sigma: '))
    print("")
    initials = [h, Mo, sigma]

# Importing the module that is used in the optimization, running the optimization
# and calculating the uncertainties of the optimized parameters:
    from scipy.optimize import curve_fit
    best, covariance = curve_fit(gauss_function, x, y, p0=initials)
    error = np.sqrt(np.diag(covariance))

# Printing the values and uncertainties gotten from the optimization:
    print("Valores e Incertezas da Optimização:")
    first = "Valor optimizado da altura máxima (h) = {} +- {}".format(best[0], error[0])
    second = "Valor optimizado da massa invariante (Mo) = {} +- {}".format(best[1], error[1])
    third = "Valor optimizado do desvio padrão (sigma) = {} +- {}".format(best[2], error[2])
    print(first)
    print(second)
    print(third)
        
# Plotting the histogram with the Gaussian adjust:
    plt.hist(limitedmasses, bins=300, range=(lowerlimit,upperlimit))
    plt.plot(x, gauss_function(x, *best), 'r-', label='h = {}, Mo = {}'.format(best[0], best[1]))
    plt.xlabel('Invariant mass [GeV]')
    plt.ylabel('Number of events')
    plt.title('The Gaussian fit \n')
    plt.legend()
    plt.show()

# If the peak of the boson Z was chosen, the following histogram can be plotted:
if ajuste == 2:
    print('Histograma abaixo revela o pico do bóson Z:')
    lowerlimit = 70
    upperlimit = 110
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]
    plt.hist(limitedmasses, bins=100, range=(lowerlimit,upperlimit))
    plt.xlabel('Invariant mass [GeV]')
    plt.ylabel('Number of events')
    plt.title('The Breit-Wigner fit \n')
    plt.show()

# In y-axis, the number of events per bin, which can be got from the variable 'histogram'.
# In x-axis, the centers of the bins.
    histogram = plt.hist(limitedmasses, bins=100, range=(lowerlimit,upperlimit))
    y = histogram[0]
    x = 0.5*(histogram[1][0:-1] + histogram[1][1:])
    # print('center of the bins =', x)
    # print('number of events per bin =', y)

# Defining a function that describes the Breit-Wigner distribution for the fit:
    def breitwigner(M, FWHM, Mo, a, b, A):
        return a*M+b+A*((2*np.sqrt(2)*Mo*FWHM*np.sqrt(Mo**2*(Mo**2+FWHM**2)))/(np.pi*np.sqrt(Mo**2+np.sqrt(Mo**2*(Mo**2+FWHM**2)))) )/((M**2-Mo**2)**2+Mo**2*FWHM**2)

    print('Uma curva Breit-Wigner ajusta bem este histograma caso o usuário entre com valores adequados de FWHM, Mo, a, b, A.')
    print('FWHM representa um chute inicial da largura à meia-altura.')
    print('Mo representa um chute inicial da massa invariante correspondente a esta FWHM.')
    print('a representa um chute inicial da inclinação usada para notar o efeito de background.')
    print('b representa um chute inicial da intersecção em y usada para notar o efeito de background.')
    print('A representa um chute inicial da altura da distribuição Breit-Wigner. \n')
           
# Initial values for the optimization in the following order:
    FWHM = float(input('Valor inicial da largura à meia-altura FWHM: '))
    Mo = float(input('Valor inicial da massa invariante Mo: '))
    a = float(input('Valor inicial da inclinação usada para notar o efeito de background a: '))
    b = float(input('Valor inicial da intersecção em y usada para notar o efeito de background b: '))
    A = float(input('Valor inicial da altura da distribuição Breit-Wigner A: '))
    print("")
    initials = [FWHM, Mo, a, b, A]

# Import the module used in the optimization, running the optimization
# and calculating the uncertainties of the optimized parameters:
    from scipy.optimize import curve_fit
    best, covariance = curve_fit(breitwigner, x, y, p0=initials, sigma=np.sqrt(y))
    error = np.sqrt(np.diag(covariance))

# Printing the values and uncertainties gotten from the optimization:
    print("Valores e Incertezas da Optimização:")
    first = "Valor optimizado da largura à meia-altura (FWHM) = {} +- {}".format(best[0], error[0])
    second = "Valor optimizado da massa invariante (Mo) = {} +- {}".format(best[1], error[1])
    third = "Valor optimizado de a = {} +- {}".format(best[2], error[2])
    fourth = "Valor optimizado de b = {} +- {}".format(best[3], error[3])
    fifth = "Valor optimizado de A = {} +- {}".format(best[4], error[4])
    print(first)
    print(second)
    print(third)
    print(fourth)
    print(fifth)

# Plotting the histogram with the Breit-Wigner adjust:
    plt.hist(limitedmasses, bins=100, range=(lowerlimit,upperlimit))
    plt.plot(x, breitwigner(x, *best), 'r-', label='FWHM = {}, Mo = {}'.format(best[0], best[1]))
    plt.xlabel('Invariant mass [GeV]')
    plt.ylabel('Number of events')
    plt.title('The Breit-Wigner fit \n')
    plt.legend()
    plt.show()
