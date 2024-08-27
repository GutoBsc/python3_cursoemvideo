def contador(inicio, fim, passo):
    print('-='*15)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if passo < 0:
        passo = passo*-1
    if inicio <= fim:
        for i in range(inicio, fim+1, passo):
            print(i, end=' ')
    else:
        for i in range(inicio, fim-1, passo*-1):
            print(i, end=' ')
    print(' FIM!')

contador(1, 10, 1)
contador(10, 0, 2)

print('-='*15)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
contador(20, 10, -1)