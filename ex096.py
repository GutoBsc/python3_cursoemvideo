def area(l, c):
    area = l*c
    print(f'A área do terreno {l}X{c} é de {area}m².')


print(' Controle de terrenos.')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)