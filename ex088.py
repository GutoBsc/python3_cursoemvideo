from random import randint
palpites = list()
jogo = list()
sort = 0
print('='*30)
print(f'{' JOGO DA MEGASENA ':-^30}')
print('='*30)
n_jogos = int(input('Quantos jogos você deseja que eu gere? '))
for j in range(0, n_jogos):
    for i in range(0,6):
        sort = randint(1, 60)
        while sort in palpites:
            sort = randint(1, 60)
        jogo.append(sort)
    jogo.sort()
    palpites.append(jogo[:])
    jogo.clear()

print('='*30)
print(f'Segue abaixo os palpites gerados para os {n_jogos} jogos:')
for i in range(0, n_jogos):
    print(f'Jogo {i+1}: {palpites[i]}')
print(f'{' BOA SORTE!! ':=^30}')