r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        tri = 'equilatero'
    elif r1 == r2 or r1 == r3 or r2 == r3:
        tri = 'isóceles'
    else:
        tri = 'escaleno'
    print('Será formado um triângulo \033[4;35m{}\033[m.'.format(tri))
else:
    print('Essas 3 retas não podem formar um triângulo.')