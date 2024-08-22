pessoa = list()
galera = list()
menor_peso = maior_peso = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))

    if len(galera) == 0:
        menor_peso = maior_peso = pessoa[1]
    else:
        if pessoa[1] > maior_peso:
            maior_peso = pessoa[1]
        if pessoa[1] < menor_peso:
            menor_peso = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()
    parar_lasso = str(input('Deseja adicionar mais alguma pessoa? [S/N]: ')).upper()
    if  parar_lasso == 'N':
            break
    elif parar_lasso == 'S':
        print('.'* 25)
    else:
        while parar_lasso != 'S' and parar_lasso != 'N':
            parar_lasso = str(input('Opção inválida! Digite novamente [S/N]: ')).upper()
    pessoa.clear()
print('* ' * 20)
print(galera)
print(f'No total foram cadastradas {len(galera)} pessoas.')
print(f'O maior peso encontrado foi de {maior_peso}Kg. Peso da(s) pessoa(s): ', end='')
for g in galera:
    if g[1] == maior_peso:
        print(f'[{g[0]}] ', end='')
print()
print(f'O menor peso encontrado foi de {menor_peso}Kg. Peso da(s) pessoa(s): ', end='')
for g in galera:
    if g[1] == menor_peso:
        print(f'[{g[0]}] ', end='')
print()