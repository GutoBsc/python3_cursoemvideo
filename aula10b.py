n1 = float(input('Digite sua nota da P1: '))
n2 = float(input('Digite sua nota da P2: '))
m = (n1+n2)/2
print('A sua média foi {}'.format(m))

if m >= 5:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado.')