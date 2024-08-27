def maior(lst):
    valor_maior = 0
    print(f'-='*15)
    print('Analisando os valores passados...')
    for i in lst:
        if i > valor_maior:
            valor_maior = i
        print(f'{i}', end=' ')
    print(f'Foram informados {len(lst)} no total.')
    print(f'O maior valor informado foi {valor_maior}.')


maior([2, 9, 4, 5, 7, 1])
maior([4, 7, 0])
maior([1, 2])
maior([6])
maior([])
