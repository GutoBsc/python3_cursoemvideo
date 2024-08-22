matriz = list()
linha = list()
for m in range(0,3):
    for l in range(0,3):
        linha.append(int(input(f'Digite o valor da coluna {m} e índice {l}: ')))
    matriz.append(linha[:])
    linha.clear()
print('='*20)
print('RESULTADO DA MATRIZ:')
for l in range(0,3):
    for e in range(0,3):
        print(f'[{matriz[l][e]:^5}]  ', end='')
    print()