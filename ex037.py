num = int(input('Digite um número inteiro: '))
base = int(input('''Vamos converter a base desse número!
Escolha uma das três bases a seguir e escreva igual está escrito abaixo:
1 - binário
2 - octal
3 - hexadecimal
Escreva aqui o número da opção escolhida: '''))

if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')

