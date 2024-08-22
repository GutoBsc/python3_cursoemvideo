matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
som_par = som_ter_col = som_seg_linha = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor da coluna {l} e índice {c}: '))
print('='*20)
print('RESULTADO DA MATRIZ:')
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            som_par += matriz[l][c]
        if c == 2:
            som_ter_col += matriz[l][c]
        if l == 2:
            som_seg_linha += matriz[l][c]
        print(f'[{matriz[l][c]:^5}]  ', end='')
    print()
print('='*20)
print(f'A soma dos valores pares é igual a {som_par}.')
print(f'A soma da terceira coluna é igual a {som_ter_col}.')
print(f'A soma da segunda linha é igual a {som_seg_linha}.')
