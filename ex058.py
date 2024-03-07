from random import randint
n = randint(0, 100)
acertou = False
cont = 0
print('Vou pensar em um número entre 0 e 10.')
while not acertou:
    chute = int(input('Tente adivinhar o número: '))
    cont += 1
    if chute == n:
        acertou = True
    else:
        if chute < n:
            print('Mais... Tente mais uma vez!')
        elif chute > n:
            print('Menos... Tente mais uma vez!')
print('Parabéns! Você acertou o número, e levou {} tentativas para acertar.'.format(cont))
