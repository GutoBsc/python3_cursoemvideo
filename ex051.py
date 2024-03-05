n = int(input('Digite o primeiro termo de uma progressão aritmética: '))
r = int(input('Qual a razão dessa progressão?: '))
dec = n + (10 - 1) * r
for c in range(n, dec + 1, r):
    print('O {:.0f}º termo é {}.'.format(((c-n)/r)+1, c))