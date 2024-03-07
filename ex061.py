n = int(input('Digite o primeiro termo de uma progressão aritmética: '))
r = int(input('Digite a razão dessa P.A.: '))
termo = n
cont = 1
while cont <= 10:
    print('O {}º termo é {}.'.format(cont, termo))
    termo = n + cont*r
    cont += 1
