class Dobrar:

    def dobrar_elementos(uma_lista):
        for (i, valor) in enumerate(uma_lista):
            novo_elem = 2 * valor
            uma_lista[i] = novo_elem
        return uma_lista
