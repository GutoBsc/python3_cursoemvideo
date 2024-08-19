frase = input('Digite a expressão matemática aqui:')
cont_abr = 0
cont_fec = 0
for c in range(0, len(frase)):
    if frase[c] == '(':
        cont_abr += 1
    if frase[c] == ')':
        cont_fec += 1
if frase.index('(') > frase.index(')') or cont_abr != cont_fec:
    print('Sua expressão está incorreta.')
else:
    print('Sua expressão está correta!')