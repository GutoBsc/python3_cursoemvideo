a = [2, 3, 4, 7]
b = a[:] #Cria uma cópia de A dentro de B, sem deixar as listas conectadas
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
