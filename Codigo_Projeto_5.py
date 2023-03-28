import numpy as np
import time
import matplotlib.pyplot as plt


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


values = [0, 1, 2, 4]

for i in values:
    matriz2 = np.array(matriz)
    elements = i
    quantity = np.count_nonzero(matriz2 == i)
    print(f'Elemento {elements} apareceu {quantity} vezes')
    print(f'Soma: {elements*quantity}')

def fib(elements):
    if elements <= 1:
        return elements
    return fib(elements - 1) + fib(elements - 2)

ns = []
tempos = []

for elements in range(1, 31):
    start = time.perf_counter()
    result= fib(elements)
    end = time.perf_counter()
    ms = (end-start) * 10**6
    ns.append(elements)
    tempos.append(ms)
print(result)
# cria o gráfico
plt.plot(ns, tempos)
plt.xlabel('Valor de elements')
plt.ylabel('Tempo de execução (micro segundos)')
plt.show()
