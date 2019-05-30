def dobrar_elementos(uma_lista):

    """ Reescreve os elementos de uma_lista com o dobro de seus valores originais. """
    
    clone_lista = uma_lista[:]
    for (i, valor) in enumerate(clone_lista):
        novo_elem = 2 * valor
        clone_lista[i] = novo_elem

    return clone_lista

minha_lista = [2, 4, 6]
print('lista de entrada é:', minha_lista)
print('lista dobrada é:', dobrar_elementos(minha_lista))
