# Se cada livro custa 24.95 reais, mas as livrarias têm desconto de 40% em cada, então sem contar ainda o preço da entrega, para comprar 60 livros elas têm de desembolsar:
preço = 24.95 
desconto = 0.4
numero_livros = 60
custo_compra = numero_livros*(1-desconto)*preço 

# No entanto, há ainda o preço da entrega, que é de 3 reais para o primeiro livro e 0.75 reais para cada um dos demais. Como são 60 livros, o gasto com a entrega é de:
entrega_primeiro = 3 
entrega_demais = 0.75
custo_entrega = entrega_primeiro + (numero_livros-1)*entrega_demais

# Logo, o custo total é de:
custo_total = custo_compra + custo_entrega
print('o custo total da compra dos 60 livros é de aproximadamente', round(custo_total,2), 'reais')

