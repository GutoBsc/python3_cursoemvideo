t1 = 0
t2 = 1
cont = 1
n = int(input('Digite um número inteiro que será o numero de termos iniciais da sequência de Fibonacci exibidos na tela: '))
print('-'*23)
print('Sequência de Fibonacci')
print('-'*23)
print('{}  -->  {}  '.format(t1, t2), end='')
while cont <= (n - 2):
    t3 = t1 + t2
    print('-->  {}  '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM.')
