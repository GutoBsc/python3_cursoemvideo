nome = input('Digite seu nome completo: ').strip()
lista = nome.split()

print(nome.upper())
print(nome.lower())
print('O nome completo tem {} letras.'.format(len(''.join(lista))))
print('O primeiro nome tem {} letras.'.format(len(lista[0])))