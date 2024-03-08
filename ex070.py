soma = mais_mil = maior_p = menor_p = n = 0
prod_barato = ''
print('=' * 20)
print('SUPERMERCADO BARATÃO')
print('=' * 20)
while True:
    n += 1
    print('Cadastre um produto:')
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: R$'))
    soma += preço
    if preço > maior_p:
        maior_p = preço
    if preço > 1000:
        mais_mil += 1
    if n == 1 or preço < menor_p:
        menor_p = preço
        prod_barato = nome
    while True:
        continuar = str(input('Você quer continuar? [S/N]')).upper()
        if continuar in 'SN':
            break
    print('-'*20)
    if continuar == 'N':
        break
print('='*20)
print(f'''RESULTADOS:
Total gasto: R${soma}
Total de produtos de mais de R$1000: {mais_mil}
Produto mais barato: {prod_barato}''')
