n_cin = n_vin = n_dez = n_um = 0
print('=' * 20)
print('CAIXA ELETRÔNICO')
print('=' * 20)
valor = int(input('Digite o valor que deseja sacar (sem centavos): '))
n_cin = valor // 50
valor = valor % 50
n_vin = valor // 20
valor = valor % 20
n_dez = valor // 10
valor = valor % 10
n_um = valor
print(F'''Quantidades de cada nota:
R$50 - {n_cin} notas.
R$20 - {n_vin} notas.
R$10 - {n_dez} notas.
R$1 - {n_um} notas.''')
