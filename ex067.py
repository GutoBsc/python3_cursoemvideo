while True:
    n = int(input('Digite um número para ver sua a tabuada, ou um valor negativo para fechar o programa:  '))
    if n < 0:
        break
    for c in range(0, 11):
        print('{} x {:2} = {}'.format(n, c, n * c))
    print('-'*30)
print('FIM.')
