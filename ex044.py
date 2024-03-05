print('{:=^40}'.format(' LOJAS AUGUSTO´S '))
preco = float(input('Digite o preço original do produto: R$'))
cond = int(input('Formas de pagamento: \n 1 - À vista no dinheiro. \n 2 - À vista no cartão. \n 3 - 2x no cartão. \n 4 - 3x ou mais no cartão. \n Escolha uma opção: '))
if cond >= 1 and cond <=4:
    if cond == 1:
        preco = preco*0.9
    elif cond == 2:
        preco = preco*0.95
    elif cond == 3:
        preco = preco
    else:
        preco = preco*1.2
    print('O preço do produto atualizado à condição escolhida é de R${}'.format(preco))
else:
    print('\033[31mOpção inválida!\033[m Tente novamente.')