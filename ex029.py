vel = int(input('Digite a velocidade do carro em km/h: '))
if vel <= 80:
    print('Você está dentro do limite de velocidade!')
else:
    print('Você ultrapassou o limite de velocidade em {} km/h, a multa custa R${}'.format((vel-80), (7*(vel-80))))