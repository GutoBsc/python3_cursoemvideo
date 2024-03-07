s = ''
masc = fem = 0
while s != 'M' and s != 'F':
    s = str(input('Digite o seu sexo [M/F]: ')).upper()
    if s == 'M':
        print('A pessoa é do sexo masculino!')
    elif s == 'F':
        print('A pessoa é do sexo feminino!')
    else:
        print('Opção inválida, tente novamente.')
