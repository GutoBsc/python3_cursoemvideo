n = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont +=1
        print('\033[32m{}\033[m'.format(c), end=' ')
    else:
        print('\033[31m{}\033[m'.format(c), end = ' ')
if cont == 2:
    print('\n{} é um número primo!!!'.format(n))
else:
    print('\nO número {} não é um número primo e é divisível {} vezes.'.format(n, cont))
