boletim = list()
nomes = list()
n1 = list()
n2 = list()
medias = list()
parar_lasso = tot_alunos = 0
while True:
    nomes.append(str(input('Digite o nome do aluno: ')))
    n1.append(float(input('Digite a nota dele(a) na P1: ')))
    n2.append(float(input('Digite a nota dele(a) na P2: ')))
    tot_alunos += 1
    parar_lasso = str(input('Deseja adicionar mais alguma pessoa? [S/N]: ')).upper()
    while parar_lasso != 'S' and parar_lasso != 'N':
        parar_lasso = str(input('Opção inválida! Digite novamente [S/N]: ')).upper()
    if  parar_lasso == 'N':
            break
    elif parar_lasso == 'S':
        print('.'* 25)
print('='*24)
print('Aqui está a tabela dos alunos e suas médias:')
for i in range(0, tot_alunos):
    medias.append((n1[i] + n2[i]) / 2)
for i in range(0, tot_alunos):
    boletim.append(nomes)
    boletim.append(n1)
    boletim.append(n2)
    boletim.append(medias)
for a in range(0, tot_alunos):
    print(f'O aluno {boletim[0][a]} obteve a média final igual a {boletim[3][a]}.')
print('='*24)
while True:
    ver_notas = str(input('Você deseja ver a tabela de notas completa dos alunos? [S/N]: ')).upper()
    while ver_notas not in 'S' and ver_notas not in 'N':
        ver_notas = str(input('Opção inválida! Digite novamente [S/N]: ')).upper()
    if  ver_notas == 'N':
            break
    elif ver_notas == 'S':
        for a in range(0, tot_alunos):
            print(f'O aluno {boletim[0][a]} obteve a nota da P1 igual a {boletim[1][a]} e da P2 igual a {boletim[2][a]}.')
        break