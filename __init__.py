def moeda(a):
    moeda = f'R${a:.2f}'.replace('.', ',')
    return moeda


def metade(a, p=False):
    metade = a/2
    if p == True:
        metade = moeda(metade)
    return metade


def dobro(a, p=False):
    dobro = a*2
    if p == True:
        dobro = moeda(dobro)
    return  dobro


def aumentar(a, b, p=False):
    aument = a*((100+b)/100)
    if p == True:
        aument = moeda(aument)
    return aument


def diminuir(a, b, p=False):
    dimin = a*((100-b)/100)
    if p == True:
        dimin = moeda(dimin)
    return dimin

def resumo(a, b, c):
    print('-'*30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-'*30)
    print(f'{'Preço analisado:':<20}{moeda(a)}')
    print(f'{'Dobro do preço:':<20}{dobro(a, True)}')
    print(f'{'Metade do preço:':<20}{metade(a, True)}')
    print(f'{b}{'% de aumento:':<18}{aumentar(a, b, True)}')
    print(f'{c}{'% de redução:':<18}{diminuir(a, c, True)}')
    print('-'*30)
