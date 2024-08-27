from random import randint
def sorteia(num):
    print('Sorteano 5 valores da lista: ', end='')
    for i in range(0, 5):
        num.append(randint(1, 10))
        print(f'{i} ', end='')
    print('PRONTO!')


def soma_par(num):
    soma = 0
    for i in num:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {num}, temos {soma}.')


numeros = []
sorteia(numeros)
soma_par(numeros)