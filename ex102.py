def fatorial(num, show=0):
    """
    -> Calucla o Fatorial e um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número.
    """
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show == True:
            if i != 1:
                print(f'{i} x ', end='')
            else:
                print(f'{i} = ', end='')
    print(f)


# Programa Principal
n = int(input('Número fatorial: '))
s = int(input('Deseja ver a conta inteira? [Digite 1 para ver]:'))
if s == 1:
    s = True
else:
    s = False
print('-*-'*10)
print(f'{'RESULTADO':-^30}')
print('-*-'*10)
fatorial(n, s)
help(fatorial )