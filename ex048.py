soma = 0
for c in range(0, 501, 3):
    if c % 2 == 1:
        soma += c
print('A soma dos números ímpares multiplos de 3 entre 1 e 500 é igual a {}'.format(soma))
