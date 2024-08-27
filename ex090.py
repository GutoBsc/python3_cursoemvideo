aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
sit = ''
if aluno['media'] >=7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] > 3 and aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-='*20)
print(f'Nome é igual {aluno['nome']}.')
print(f'Média é igual a {aluno['media']}')
print(f'Situação é igual a {aluno['situacao']}')