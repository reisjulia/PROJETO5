import numpy as np

matriz = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

coordinates = {}

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        element = matriz[i][j]
        if element not in coordinates:
            coordinates[element] = []
        coordinates[element].append((i, j))

for element in sorted(coordinates.keys()):
    print(f'{element}')
    for coord in coordinates[element]:
        print(f'{coord}')

freq = {}

values = [0, 1, 2, 4]

for i in values:
    matriz2 = np.array(matriz)
    elements = i
    quantity = np.count_nonzero(matriz2 == i)
    print(f'Elemento {elements} apareceu {quantity} vezes')
    print(f'Soma: {elements*quantity}')
