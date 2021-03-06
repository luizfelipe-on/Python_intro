# Importing the modules:
import math
import numpy as np
import pandas as pd
from scipy import special
import matplotlib.pyplot as plt
from scipy.stats import chisquare

# Importing the datafile and saving it in the variable 'ds':
ds = pd.read_csv('DoubleMuRun2011A.csv')

# Calculating the invariant mass of all pairs of muons:
invariant_mass = np.sqrt(2*ds.pt1*ds.pt2*(np.cosh(ds.eta1-ds.eta2)-np.cos(ds.phi1-ds.phi2)))

# Defining whick peak will be adjusted:
ajuste = int(input('Qual pico você quer ajustar? Digite 1 para J/psi, 2 para upsilon ou 3 para bóson Z: '))

# If the peak of J/psi was chosen, the following histogram can be plotted:
if ajuste == 1:
    print('Histograma abaixo revela o pico de J/psi:')
    lowerlimit = 2.8 
    upperlimit = 3.4
    bars = 400
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]
    histogram = plt.hist(limitedmasses, bins=bars, range=(lowerlimit,upperlimit))
    plt.xlabel('Invariant mass [GeV]')
    plt.ylabel('Number of events')
    plt.title('J/psi peak histogram \n')
    plt.show()

# In y-axis, the number of events per bin, which can be got from the variable 'histogram'.
# In x-axis, the centers of the bins.
    y = histogram[0]
    x = 0.5*(histogram[1][0:-1] + histogram[1][1:])

# Defining a function that describes the Breit-Wigner distribution for the fit:
    def breitwigner(M, FWHM, Mo, a, b, A):
        return a*M+b+A*((2*np.sqrt(2)*Mo*FWHM*np.sqrt(Mo**2*(Mo**2+FWHM**2)))/(np.pi*np.sqrt(Mo**2+np.sqrt(Mo**2*(Mo**2+FWHM**2)))) )/((M**2-Mo**2)**2+Mo**2*FWHM**2)

    print('Uma curva Breit-Wigner ajusta bem este histograma caso o usuário entre com valores adequados de FWHM, Mo, a, b, A:')
    print('FWHM representa a largura à meia-altura;')
    print('Mo representa a massa invariante correspondente a esta FWHM;')
    print('a representa a inclinação usada para notar o efeito de background;')
    print('b representa a intersecção em y usada para notar o efeito de background;')
    print('A representa a altura da distribuição Breit-Wigner. \n')
           
# Initial values for the optimization in the following order:
    print('I) Suposições Iniciais:')
    FWHM = float(input('Suposição inicial da largura à meia-altura (FWHM): '))
    Mo = float(input('Suposição inicial da massa invariante (Mo): '))
    a = float(input('Suposição inicial da inclinação usada para notar o efeito de background (a): '))
    b = float(input('Suposição inicial da intersecção em y usada para notar o efeito de background (b): '))
    A = float(input('Suposição inicial da altura da distribuição Breit-Wigner (A): '))
    print("")
    initials = [FWHM, Mo, a, b, A]

# Importing the module used in the optimization, running the optimization
# and calculating the uncertainties of the optimized parameters:
    from scipy.optimize import curve_fit
    best, covariance = curve_fit(breitwigner, x, y, p0=initials, sigma=np.sqrt(y))
    error = np.sqrt(np.diag(covariance))
    
# Taking the new parameters and optimizing them even more, until they can not be optimized anymore:
    while abs(Mo-best[1]) != 0:
        FWHM = best[0]
        Mo = best[1]
        a = best[2]
        b = best[3]
        A = best[4]
        initials = [FWHM, Mo, a, b, A]
        best, covariance = curve_fit(breitwigner, x, y, p0=initials, sigma=np.sqrt(y))
        error = np.sqrt(np.diag(covariance))

# Printing the best values and uncertainties gotten from the optimization:
    print('II) Valores e Incertezas da Optimização:')
    first = "Valor optimizado da largura à meia-altura (FWHM) = {} +- {}".format(best[0], error[0])
    second = "Valor optimizado da massa invariante (Mo) = {} +- {}".format(best[1], error[1])
    third = "Valor optimizado da inclinação (a) = {} +- {}".format(best[2], error[2])
    fourth = "Valor optimizado da intersecção em y (b) = {} +- {}".format(best[3], error[3])
    fifth = "Valor optimizado da altura da distribuição (A) = {} +- {}".format(best[4], error[4])
    print(first)
    print(second)
    print(third)
    print(fourth)
    print(fifth)
        
# Plotting the histogram with the Breit-Wigner adjust:
    plt.hist(limitedmasses, bins=bars, range=(lowerlimit,upperlimit))
    plt.plot(x, breitwigner(x, *best), 'r-', label='Mo = {}'.format(best[1]))
    plt.xlabel('Invariant mass [GeV]')
    plt.ylabel('Number of events')
    plt.title('The Breit-Wigner fit \n')
    plt.legend()
    plt.show()
    
# Determining if the invariant mass obtained in the adjust is compatible with the literature one:
    M_reference = 3.0969
    M_adjusted = best[1]
    uncertainty = error[1]
    
    print('III) Compatibilidade entre as massas do ajuste e da literatura:')
    print('De acordo com a literatura, a massa de J/psi é de', M_reference, 'GeV.')
    print('A massa obtida no ajuste foi de', M_adjusted, 'GeV.')
    
    if abs(M_adjusted-M_reference) <= 2*uncertainty:
        print('Segundo o teste de compatibilidade, a massa do ajuste É compatível com a da literatura. \n')
    else:
        print('Segundo o teste de compatibilidade, a massa do ajuste NÃO é compatível com a da literatura. \n')
        
# Applying the chi-square statistic test to verify the quality of the fit.
# After estimating the chi-square, we must normalize it by dividing it by the number of freedom degrees.
# PS: number of freedom degrees = number of bins - number of parameters of the function:    
    z = [breitwigner(lowerlimit, best[0], best[1], best[2], best[3], best[4])]
    
    for i in range(bars-1):
        k = lowerlimit + i*(upperlimit - lowerlimit)/bars
        l = breitwigner(k, best[0], best[1], best[2], best[3], best[4])
        z.append(l)
    
    divergencia, valorp = chisquare(f_obs = y, f_exp = z)

    num_param = len(initials)
    norm_divergencia = divergencia/(bars-num_param)
    
    print('IV) Teste do chi-quadrado:')
    print('Quanto mais próximo de um for o valor do chi-quadrado normalizado, melhor a qualidade do ajuste.')
    print('Neste caso, o chi-quadrado normalizado foi de aproximadamente', round(norm_divergencia,3), ', logo o ajuste é adequado.')
    
# If the peak of upsilon was chosen, the following histogram can be plotted:
if ajuste == 2:
    print('Histograma abaixo revela o pico de upsilon:')
    lowerlimit = 9.25 
    upperlimit = 9.65
    bars = 300
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]
    histogram = plt.hist(limitedmasses, bins=bars, range=(lowerlimit,upperlimit))
    plt.xlabel('Invariant mass [GeV]')
    plt.ylabel('Number of events')
    plt.title('Upsilon peak histogram \n')
    plt.show()

# In y-axis, the number of events per bin, which can be got from the variable 'histogram'.
# In x-axis, the centers of the bins.
    y = histogram[0]
    x = 0.5*(histogram[1][0:-1] + histogram[1][1:])

# Defining a function that describes Gauss distribution for the fit:
    def gauss_function(M, h, Mo, sigma):
        return h*np.exp(-(M-Mo)**2/(2*sigma**2))
    
    print('Uma curva Gaussiana ajusta bem este histograma caso o usuário entre com valores adequados de h, Mo e sigma:')
    print('h representa a altura do pico da distribuição;')
    print('Mo representa a massa invariante correspondente a esta altura;')
    print ('sigma representa o desvio padrão da distribuição.')
    print('DICA: Em uma distribuição gaussiana, o desvio padrão vale aproximadamente metade da largura à meia-altura. \n')
          
# Initial values for the optimization in the following order:
    print('I) Suposições Iniciais:')
    h = float(input('Suposição inicial da altura máxima (h): '))
    Mo = float(input('Suposição inicial da massa invariante (Mo): '))
    sigma = float(input('Suposição inicial do desvio padrão (sigma): '))
    print("")
    initials = [h, Mo, sigma]

# Importing the module that is used in the optimization, running the optimization
# and calculating the uncertainties of the optimized parameters:
    from scipy.optimize import curve_fit
    best, covariance = curve_fit(gauss_function, x, y, p0=initials, sigma=np.sqrt(y))
    error = np.sqrt(np.diag(covariance))
    
# Taking the new parameters and optimizing them even more, until they can not be optimized anymore:
    while abs(Mo-best[1]) != 0:
        h = best[0]
        Mo = best[1]
        sigma = best[2]
        initials = [h, Mo, sigma]
        best, covariance = curve_fit(gauss_function, x, y, p0=initials, sigma=np.sqrt(y))
        error = np.sqrt(np.diag(covariance))
    
# Printing the best values and uncertainties gotten from the optimization:
    print('II) Valores e Incertezas da Optimização:')
    first = "Valor optimizado da altura máxima (h) = {} +- {}".format(best[0], error[0])
    second = "Valor optimizado da massa invariante (Mo) = {} +- {}".format(best[1], error[1])
    third = "Valor optimizado do desvio padrão (sigma) = {} +- {}".format(best[2], error[2])
    print(first)
    print(second)
    print(third)
        
# Plotting the histogram with the Gaussian adjust:
    plt.hist(limitedmasses, bins=bars, range=(lowerlimit,upperlimit))
    plt.plot(x, gauss_function(x, *best), 'r-', label='Mo = {}'.format(best[1]))
    plt.xlabel('Invariant mass [GeV]')
    plt.ylabel('Number of events')
    plt.title('The Gaussian fit \n')
    plt.legend()
    plt.show()
    
# Determining if the invariant mass obtained in the adjust is compatible with the literature one:
    M_reference = 9.4603026
    M_adjusted = best[1]
    uncertainty = error[1]
    
    print('III) Compatibilidade entre as massas do ajuste e da literatura:')
    print('De acordo com a literatura, a massa de upsilon é de', M_reference, 'GeV.')
    print('A massa obtida no ajuste foi de', M_adjusted, 'GeV.')
    
    if abs(M_adjusted-M_reference) <= 2*uncertainty:
        print('Segundo o teste de compatibilidade, a massa do ajuste É compatível com a da literatura. \n')
    else:
        print('Segundo o teste de compatibilidade, a massa do ajuste NÃO é compatível com a da literatura. \n')
        
# Applying the chi-square statistic test to verify the quality of the fit.
# After estimating the chi-square, we must normalize it by dividing it by the number of freedom degrees.
# PS: number of freedom degrees = number of bins - number of parameters of the function:    
    z = [gauss_function(lowerlimit, best[0], best[1], best[2])]
    
    for i in range(bars-1):
        k = lowerlimit + i*(upperlimit - lowerlimit)/bars
        l = gauss_function(k, best[0], best[1], best[2])
        z.append(l)
    
    divergencia, valorp = chisquare(f_obs = y, f_exp = z)

    num_param = len(initials)
    norm_divergencia = divergencia/(bars-num_param)
    
    print('IV) Teste do chi-quadrado:')
    print('Quanto mais próximo de um for o valor do chi-quadrado normalizado, melhor a qualidade do ajuste.')
    print('Neste caso, o chi-quadrado normalizado foi de aproximadamente', round(norm_divergencia,3), ', logo o ajuste é adequado.')

# If the peak of the boson Z was chosen, the following histogram can be plotted:
if ajuste == 3:
    print('Histograma abaixo revela o pico do bóson Z:')
    lowerlimit = 70
    upperlimit = 110
    bars = 400
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]
    histogram = plt.hist(limitedmasses, bins=bars, range=(lowerlimit,upperlimit))
    plt.xlabel('Invariant mass [GeV]')
    plt.ylabel('Number of events')
    plt.title('Boson Z peak histogram \n')
    plt.show()

# In y-axis, the number of events per bin, which can be got from the variable 'histogram'.
# In x-axis, the centers of the bins.
    y = histogram[0]
    x = 0.5*(histogram[1][0:-1] + histogram[1][1:])

# Defining a function that describes the Breit-Wigner distribution for the fit:
    def breitwigner(M, FWHM, Mo, a, b, A):
        return a*M+b+A*((2*np.sqrt(2)*Mo*FWHM*np.sqrt(Mo**2*(Mo**2+FWHM**2)))/(np.pi*np.sqrt(Mo**2+np.sqrt(Mo**2*(Mo**2+FWHM**2)))) )/((M**2-Mo**2)**2+Mo**2*FWHM**2)

    print('Uma curva Breit-Wigner ajusta bem este histograma caso o usuário entre com valores adequados de FWHM, Mo, a, b, A:')
    print('FWHM representa a largura à meia-altura;')
    print('Mo representa a massa invariante correspondente a esta FWHM;')
    print('a representa a inclinação usada para notar o efeito de background;')
    print('b representa a intersecção em y usada para notar o efeito de background;')
    print('A representa a altura da distribuição Breit-Wigner. \n')
           
# Initial values for the optimization in the following order:
    print('I) Suposições Iniciais:')
    FWHM = float(input('Suposição inicial da largura à meia-altura (FWHM): '))
    Mo = float(input('Suposição inicial da massa invariante (Mo): '))
    a = float(input('Suposição inicial da inclinação usada para notar o efeito de background (a): '))
    b = float(input('Suposição inicial da intersecção em y usada para notar o efeito de background (b): '))
    A = float(input('Suposição inicial da altura da distribuição Breit-Wigner (A): '))
    print("")
    initials = [FWHM, Mo, a, b, A]

# Importing the module used in the optimization, running the optimization and calculating the uncertainties of the optimized parameters:
    from scipy.optimize import curve_fit
    best, covariance = curve_fit(breitwigner, x, y, p0=initials, sigma=np.sqrt(y))
    error = np.sqrt(np.diag(covariance))
    
# Taking the new parameters and optimizing them even more, until they can not be optimized anymore:
    while abs(Mo-best[1]) != 0:
        FWHM = best[0]
        Mo = best[1]
        a = best[2]
        b = best[3]
        A = best[4]
        initials = [FWHM, Mo, a, b, A]
        best, covariance = curve_fit(breitwigner, x, y, p0=initials, sigma=np.sqrt(y))
        error = np.sqrt(np.diag(covariance))

# Printing the best values and uncertainties gotten from the optimization:
    print('II) Valores e Incertezas da Optimização:')
    first = "Valor optimizado da largura à meia-altura (FWHM) = {} +- {}".format(best[0], error[0])
    second = "Valor optimizado da massa invariante (Mo) = {} +- {}".format(best[1], error[1])
    third = "Valor optimizado da inclinação (a) = {} +- {}".format(best[2], error[2])
    fourth = "Valor optimizado da intersecção em y (b) = {} +- {}".format(best[3], error[3])
    fifth = "Valor optimizado da altura da distribuição (A) = {} +- {}".format(best[4], error[4])
    print(first)
    print(second)
    print(third)
    print(fourth)
    print(fifth)
        
# Plotting the histogram with the Breit-Wigner adjust:
    plt.hist(limitedmasses, bins=bars, range=(lowerlimit,upperlimit))
    plt.plot(x, breitwigner(x, *best), 'r-', label='Mo = {}'.format(best[1]))
    plt.xlabel('Invariant mass [GeV]')
    plt.ylabel('Number of events')
    plt.title('The Breit-Wigner fit \n')
    plt.legend()
    plt.show()
    
# Determining if the invariant mass obtained in the adjust is compatible with the literature one:
    M_reference = 91.187621
    M_adjusted = best[1]
    uncertainty = error[1]
    
    print('III) Compatibilidade entre as massas do ajuste e da literatura:')
    print('De acordo com a literatura, a massa do bóson é de', M_reference, 'GeV.')
    print('A massa obtida no ajuste foi de', M_adjusted, 'GeV.')
    
    if abs(M_adjusted-M_reference) <= 2*uncertainty:
        print('Segundo o teste de compatibilidade, a massa do ajuste É compatível com a da literatura. \n')
    else:
        print('Segundo o teste de compatibilidade, a massa do ajuste NÃO é compatível com a da literatura. \n')
        
# Applying the chi-square statistic test to verify the quality of the fit.
# After estimating the chi-square, we must normalize it by dividing it by the number of freedom degrees.
# PS: number of freedom degrees = number of bins - number of parameters of the function:    
    z = [breitwigner(lowerlimit, best[0], best[1], best[2], best[3], best[4])]
    
    for i in range(bars-1):
        k = lowerlimit + i*(upperlimit - lowerlimit)/bars
        l = breitwigner(k, best[0], best[1], best[2], best[3], best[4])
        z.append(l)
    
    divergencia, valorp = chisquare(f_obs = y, f_exp = z)

    num_param = len(initials)
    norm_divergencia = divergencia/(bars-num_param)
    
    print('IV) Teste do chi-quadrado:')
    print('Quanto mais próximo de um for o valor do chi-quadrado normalizado, melhor a qualidade do ajuste.')
    print('Neste caso, o chi-quadrado normalizado foi de aproximadamente', round(norm_divergencia,3), ', logo o ajuste é adequado.')
