matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor da coluna {l} e índice {c}: '))
print('='*20)
print('RESULTADO DA MATRIZ:')
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^5}]', end='')
    print()