cidade = input('Digite o nome da cidade: ')
cidade = cidade.upper()
lista = cidade.split()

if lista[0] == 'SANTO':
    print('A cidade tem o nome ´Santo` no começo!')
else:
    print('A cidade não tem ´Santo` no começo.')