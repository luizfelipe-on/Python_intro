# 1) Definindo uma função que responde se, com os três valores de entrada, é possível fazer um triângulo: 
def is_triangle(a,b,c):
    if a>b+c or b>a+c or c>a+b:
         print('No')
    else:
         print('Yes')

# Nos dois primeiros casos, dá para fazer um triângulo. Nos dois últimos, não:
is_triangle(3,8,6)
is_triangle(2,4,5)
is_triangle(1,5,2)
is_triangle(8,1,6)

# 2) Solicitando os valores, convertendo-os em inteiros e acionando is_triangle():
a = int(input('valores desejado do primeiro comprimento: '))
b = int(input('valores desejado do segundo comprimento: '))
c = int(input('valores desejado do terceiro comprimento: '))

is_triangle(a,b,c)
