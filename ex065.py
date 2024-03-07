maior = menor = média = soma = cont = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um valor: '))
    if cont == 0:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    cont += 1
    continuar = str(input('Você deseja continuar? [S/N]')).upper()
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Tente novamente:')).upper()
    média = soma/cont
print('''Resultados:
Você digitou {} números.
Maior número: {}
Menor número: {}
Média entre todos: {:.2f}'''.format(cont, maior, menor, média))
