print('-=-'*11)
print('Análise de empréstimo bancario.')
print('-=-'*11)
valor = float(input('Qual o valor da casa que deseja comprar? R$'))
sal = float(input('Qual o seu salário? R$'))
a = int(input('Em quantos anos você irá pagar pela casa? '))
pm = valor/(a*12)
print('Para pagar uma casa de R${} em {} anos a pestação será de R${}'.format(valor, a, pm))
if pm <= 0.3*sal:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado.')