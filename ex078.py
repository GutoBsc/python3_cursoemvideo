valores =[]
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
max = max(valores)
min = min(valores)

print(f'O maior valor encontrado foi {max}, e se encontra na(s) posição(ões) ', end='')
for c, v in enumerate(valores):
    if v == max:
        print(f'{c}... ', end='')
print('\n')
print(f'O menor valor encontrado foi {min}, e se encontra na(s) posição(ões)', end='')
for c, v in enumerate(valores):
    if v == min:
        print(f'{c}... ', end='')
print('\n')