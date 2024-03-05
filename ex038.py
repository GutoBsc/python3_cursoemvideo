n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print('O \033[33mprimeiro\033[m valor é \033[34mmaior\033[m.')
elif n1 < n2:
    print('O \033[33msegundo\033[m valor é \033[34mmaior\033[m.')
else:
    print('\033[33mNão existe\033[m valor maior, os dois são \033[34miguais\033[m.')