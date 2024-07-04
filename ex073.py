colocados = ('Flamengo', 'Palmeiras', 'Botafogo', 'Bahia', 'Atlético-PR', 'São Paulo', 'Cruzeiro', 'Fortaleza', 'Bragantino', 'Internacional', 'Atlético-MG', 'Juventude', 'Criciúma', 'Cuiabá', 'EC Vitória', 'Vasco da Gama', 'Atlético-GO', 'Grêmio', 'Corinthians', 'Fluminense')
print('*'*33)
print('CAMPEONATO BRASILEIRO DE FUTEBOL')
print('*'*33)
print('Os 5 primeiros colocados são:')
for c in range (0, 5):
    print(colocados[c])
print('*'*33)
print('Os últimos 4 colocados são:')
for c in range (-4, 0):
    print(colocados[c])
print('*'*33)
print('Em ordem alfabética, os times da séria A são:')
print(sorted(colocados))
print('*'*33)
time = str(input('Digite o nome do time que deseja saber a posição:'))
for cont, time_correto in enumerate(colocados):
    if time_correto == time:
        print(f'O time {time_correto} está na {cont+1}ª posição do campeonato.')