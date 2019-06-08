# Função modificadora que dobra o valor dos elementos de uma lista:
def dobrar_elementos(lista):
    clone_lista = lista[:]
    for (i, valor) in enumerate(clone_lista):
        valor_dobrado = 2 * valor
        clone_lista[i] = valor_dobrado
    print('lista de entrada:', lista)
    print('lista dobrada:', clone_lista)

# Escolhendo uma lista de entrada e aplicando a função: 
minha_lista = [2, 4, 6]
dobrar_elementos(minha_lista)
