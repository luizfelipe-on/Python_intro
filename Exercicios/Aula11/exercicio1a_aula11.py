# Construindo a matriz fornecida pelo enunciado:
matrix = {(0,0):0, (0,1):0, (0,2):0, (0,3):1, (0,4):0, (1,0):0, (1,1):0, (1,2):0, (1,3):0, (1,4):0,
          (2,0):0, (2,1):2, (2,2):0, (2,3):0, (2,4):0, (3,0):0, (3,1):0, (3,2):0, (3,3):0, (3,4):0,
          (4,0):0, (4,1):0, (4,2):0, (4,3):3, (4,4):0}

# Acessando os valores solicitados no exercício:
print(matrix.get((0,3)))
print(matrix.get((2,1)))
print(matrix.get((4,3)))
print(matrix.get((2,2)))
