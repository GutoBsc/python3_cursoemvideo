frase = input('Escreva uma frase: ')
frase = frase.strip()
frase_backup = frase
frase = frase.lower()
frase = frase.split()
frase = ''.join(frase)

inverso = frase[::-1]
'''inverso = ''
for letra in range(len(frase) -1, -1, -1):
    inverso += frase[letra] '''

if frase == inverso:
    print('Que legal!!! A frase `{}´ forma um palíndromo.'.format(frase_backup))
else:
    print('A frase não forma um palíndromo.')
