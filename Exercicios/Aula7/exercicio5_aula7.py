# 1) Criando a função que testa o último teorema de Fermat:
def check_fermat(a,b,c,n):
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')

# Provando que ele não se mantém:
check_fermat(0,1,1,3)

# 2) Solicitando os valores de a, b, c e n, tranformando-os em inteiros e acionando check_fermat():
a = int(input('Qual o valor de a desejado? '))
b = int(input('Qual o valor de b desejado? '))
c = int(input('Qual o valor de c desejado? '))
n = int(input('Qual o valor de n desejado? '))

check_fermat(a,b,c,n)


