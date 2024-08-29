def ficha(nome='<desconhecido>', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


j = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))
ficha(j, g)
