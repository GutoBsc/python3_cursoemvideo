from random import randint
from time import sleep
n = o
print('*'*26)
print('Jogo do PAR ou ÍMPAR')
print('*'*26)
while True:
    computador = randint(1,5)
    escolha = int(input('Digite [0] para´PAR` ou  [1] para ´Impar`: '))
    while escolha not in [0, 1]:
        print('Opção inválida, digite 0 ou 1:')
        escolha = int(input('Digite [0] para´PAR` ou  [1] para ´Impar`: '))
    jogador = int(input('Escolha um número entre 1 e 5: '))
    print(f'O computador escolheu {computador}')
    print('PROCESSANDO...')
    sleep(2)
    soma = jogador + computador
    resultado = soma % 2
    if resultado == escolha:
        print('Parabéns, você ganhou!! Jogeu mais uma vez.')
        print('-'*30)
    else:
        print('Você foi derrotado pelo computador')
        break
    n += 1
print(f'GAME OVER! Você conseguiu {n} vitórias!')
