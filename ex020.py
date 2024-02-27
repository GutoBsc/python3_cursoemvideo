from random import shuffle
n1 = input('Digite o nome do aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do teerceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem escolhida foi {}'.format(lista))


"""
if ordem == 1:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n1, n2, n3, n4))
if ordem == 2:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n1, n2, n4, n3))
if ordem == 3:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n1, n3, n2, n4))
if ordem == 4:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n1, n3, n4, n2))
if ordem == 5:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n1, n4, n3, n2))
if ordem == 6:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n1, n4, n2, n3))
if ordem == 7:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n2, n1, n3, n4))
if ordem == 8:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n2, n1, n4, n3))
if ordem == 9:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n2, n3, n1, n4))
if ordem == 10:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n2, n3, n4, n1))
if ordem == 11:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n2, n4, n3, n1))
if ordem == 12:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n2, n4, n1, n3))
if ordem == 13:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n3, n2, n1, n4))
if ordem == 14:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n3, n2, n4, n1))
if ordem == 15:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n3, n1, n2, n4))
if ordem == 16:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n3, n1, n4, n2))
if ordem == 17:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n3, n4, n1, n2))
if ordem == 18:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n3, n4, n2, n1))
if ordem == 19:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n4, n1, n3, n2))
if ordem == 20:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n4, n1, n2, n3))
if ordem == 21:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n4, n3, n1, n2))
if ordem == 22:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n4, n3, n2, n1))
if ordem == 23:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n4, n2, n3, n1))
if ordem == 24:
    print('O ordem escolhido para as apresentações foi: \n 1. {}. \n 2. {}. \n 3. {}. \n 4. {}.'.format(n4, n2, n1, n3))
"""