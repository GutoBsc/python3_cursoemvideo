from random import choice
n1 = input('Digite o nome do aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do teerceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
"""
sort = random.randint(1,4)
aluno = ''
if sort == 1:
    aluno = n1
elif sort == 2:
    aluno = n2
elif sort == 3:
    aluno = n3
else:
    aluno = n4
print('O escolhido para limpar a lousa foi o aluno {}, {}!'.format(sort, aluno))
"""