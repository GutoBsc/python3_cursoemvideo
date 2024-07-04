from random import randint
numeros = (randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50))
print(f'A lista de números é: {numeros}')
# print(f'O menor valor é {sorted(numeros)[0]}')
print(f'O menor valor é {min(numeros)}')
# print(f'O maior valor é {sorted(numeros)[4]}')
print(f'O maior valor é {max(numeros)}')