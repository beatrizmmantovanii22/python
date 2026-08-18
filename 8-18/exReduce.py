from functools import reduce

numeros = [2, 3, 4, 5]

resultado = reduce(lambda x, y: x*y, numeros)
print(resultado)
