from random import randint
from time import sleep
n = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entra 0 e 5, tente adivinhar...')
print('-=-'*20)
num = int(input('Qual búmero eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if num == n:
    print('Parabéns! Você acertou o número secreto!')
else:
    print('Infelizmente você errou o número secreto, o número era {}.'.format(n))