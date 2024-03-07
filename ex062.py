n = int(input('Digite o primeiro termo de uma progressão aritmética: '))
r = int(input('Digite a razão dessa P.A.: '))
termo = n
cont = 1
while cont <= 10:
    print('O {}º termo é {}.'.format(cont, termo))
    termo = n + cont*r
    cont += 1

perg = 1
while perg >= 0:
    perg = int(input('Se quiser continuar a progressão digete  número de termos, caso queira para digite 0:'))
    if perg > 0:
        for c in range(perg, 0, -1):
            print('O {}º termo é {}.'.format(cont, termo))
            termo = n + cont * r
            cont += 1
            perg -= 1
    else:
        print('Finalizando programa.')
        perg -= 1
