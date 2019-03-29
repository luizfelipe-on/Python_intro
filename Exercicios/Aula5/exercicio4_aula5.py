# Uma função que verificar se um determinado número está dentro de um certo intervalo é:
def verificacao(x,xmin,xmax):
    if x > xmin and x < xmax:
        print x, 'está dentro do intervalo', [xmin,xmax]
    else:
        print x, 'não está dentro do intervalo', [xmin,xmax]

verificacao(2,1,3)
verificacao(5,2,4)
verificacao(3**4,5**2,2**7)
