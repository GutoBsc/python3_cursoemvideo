def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


# Programa Principal
j = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g=0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)
