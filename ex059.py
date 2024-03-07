n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
soma = 0
mul = 0
maior = 0
op = 0
while op != 5:
    op = int(input('Qual operação você quer realizar? \n [1] - Somar \n [2] - Multiplicar \n [3] - Escolher o maior \n [4] - Escolher novos números \n [5] - Sair do programa \n Escolha a opção: '))
    if op == 1:
        soma = n1 + n2
        print('A soma dos números é {}'.format(soma))
    elif op == 2:
        mul = n1 * n2
        print('O produto dos números é {}'.format(mul))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre os dois é {}'.format(maior))
    elif op == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    elif op == 5:
        print('Saindo do programa!')
    else:
        print('Opção inválida! Tente novamente.')
    print('-'*34)