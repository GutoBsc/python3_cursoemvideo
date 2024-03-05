from random import randint
from time import sleep
print('-*-'*6)
print('\033[1;35mJogo do Jokenpô.\033[m')
print('-*-'*6)
jogador = input('Escreva a sua escolha (´Pedra`, ´Papel` ou ´Tesoura)`: ')
jogador = jogador.strip().upper()
computador = randint(1,3)
if computador == 1:
    computador = 'Pedra'
elif computador == 2:
    computador = 'Papel'
else:
    computador = 'Tesoura'
print('O computador escolheu: {}.'.format(computador))
print('PROCESSANDO...')
sleep(2)
if jogador in 'PEDRA PAPEL TESOURA':
    if jogador == 'PEDRA':
        if computador == 'Papel':
            ganhador = 'Computador'
        elif computador == 'Tesoura':
            ganhador = 'Você'
        else:
            ganhador = 'Ninguém'
    elif jogador == 'PAPEL':
        if computador == 'Tesoura':
            ganhador = 'Computador'
        elif computador == 'Pedra':
            ganhador = 'Você'
        else:
            ganhador = 'Ninguém'
    else:
        if computador == 'Pedra':
            ganhador = 'Computador'
        elif computador == 'Papel':
            ganhador = 'Você'
        else:
            ganhador = 'Ninguém'
    if ganhador == 'Você':
        print('Parabéns, você ganhou!!!')
    elif ganhador == 'Computador':
        print('Não foi dessa vez, o computador ganhou.')
    else:
        print('Empate! Não houve nenhum ganhador.')
else:
    print('Opção innválida! Tente novamente.')