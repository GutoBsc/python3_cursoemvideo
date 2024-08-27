pessoa = dict()
grupo = []
mulheres = []
mais_velhos = []
resp = media_grupo = soma_grupo = 0
while resp != 'N':
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()
    while pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
        pessoa['sexo'] = str(input('Opção inválida, digite novamente [M/F]: ')).upper()
    pessoa['idade'] = int(input('Idade: '))
    soma_grupo += pessoa['idade']
    grupo.append(pessoa.copy())
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa.clear()
    resp = str(input('Deseja adicionar mais alguém? [S/N]: ')).upper()
    while resp != 'S' and resp != 'N':
        resp = str(input('Opção inválida, digite novamente [S/N]: ')).upper()
print('-=' * 26)
print(f'A)  Foram cadastradas {len(grupo)} pessoas.')
media_grupo = soma_grupo / len(grupo)
print(f'B)  A média de idade do grupo é de {media_grupo:5.2f} anos.')
print(f'C)  Lista das mulheres do grupo: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p['nome']} ', end='')
print()
print(f'D)  Lista das pessoas que estão acima da média: ')
for i in grupo:
    if i['idade'] >= media_grupo:
        print('    ', end='')
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
