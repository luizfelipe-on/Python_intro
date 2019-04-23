# Uma forma de verificar quais números de uma lista são pares é utilizando o operador módulo (%), que fornece o resto de uma divisão.
# Sendo assim, usando '% 2' para um número inteiro, se for retornado 0 então ele é par.  
lista = [8,15,77,938,456,623]
for n in lista:
    if n % 2 == 0:
        print(n, 'é par')
