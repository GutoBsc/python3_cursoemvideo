d = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quanto kilômetros foram rodados com o carro? '))
pagar = 60*d + 0.15*km
print('O aluguel total ficou em R${:.2f}'.format(pagar))