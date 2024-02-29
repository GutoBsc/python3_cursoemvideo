nome = input('Digite seu nome completo: ')
lista = nome.split()

print('O seu primeiro nome é {} e o seu último nome é {}.'.format(lista[0], lista[len(lista)-1]))
