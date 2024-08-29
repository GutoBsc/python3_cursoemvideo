def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vário alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional indicando se deve ou não add a situação
    :return: dicionário com várias informações sobre a turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    for i, e in enumerate(n):
        if i == 0:
            maior = e
            menor = e
        if sit == True:
            if i < len(n):
                if e > r['maior']:
                    maior = e
                if e < r['menor']:
                    menor = e
    if r['média'] < 3:
        r['situacao'] = 'RUIM'
    elif r['média'] < 5:
        r['situacao'] = 'RAZOÁVEL'
    else:
        r['situacao'] = 'BOA'
    print('-='*12)
    print(f'Quantidade de notas: {r['total']}')
    print(f'Maior nota: {r['maior']}')
    print(f'Menor nota: {r['menor']}')
    print(f'Média da turma: {r['média']:.2f}')
    print(f'Situação: {r['situacao']}')


# Programa Principal
notas(5.5, 2.5, 9, 8.5, sit=True)
notas(4, 3, 10, sit=True)
notas(2, 3, 6, sit=True)
help(notas)