def recurse(n, s):
    """ É necessário n > 0 para que a função funcione, do contrário se terá uma recursividade infinita. """
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

# Para n > 0, a função funciona, retornando um valor inteiro.
recurse(3, 0)

# Para n <= 0, a função nunca atinge um caso-base, sendo retornado o erro de profundidade máxima atingida.
recurse(-1, 0)
