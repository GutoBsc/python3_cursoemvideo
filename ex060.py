n = int(input('Digite um número inteiro para calcularmos o seu fatorial: '))
resultado = n
print('{}! = {} * '.format(n, n), end = '')
while n > 1:
    n -= 1
    resultado = resultado * n
    if n > 1:
        print('{} * '.format(n), end='')
    else:
        print('{} '.format(n), end='')
print('= {}'.format(resultado))
