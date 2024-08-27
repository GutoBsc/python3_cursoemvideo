time = []
jogador = dict()
partidas = []
tot_gols = 0
resp = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input('Quantidade de partidas: '))
    partidas.clear()
    for i in range(0, tot):
        partidas.append(int(input(f'Nº de gols na partida {i+1}: ')))
        tot_gols += partidas[i]
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    resp = str(input('Deseja adicionar mais algum jogador? [S/N]: ')).upper()
    while resp != 'S' and resp != 'N':
        resp = str(input('Opção inválida, digite novamente [S/N]: ')).upper()
    if resp == 'N':
        break
    print('-'*26)
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*26)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*26)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 26)
print(' << VOLTE SEMPRE! >>')
