peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso/(altura**2)
if imc < 18.5:
    sit = 'Abaixo do peso'
elif imc <= 25:
    sit = 'Peso ideal'
elif imc <= 30:
    sit = 'Sobrepeso'
elif imc <= 40:
    sit = 'Obesidade'
else:
    sit = 'Obesidade morbida'
print('A sua situação atual é: {}.'.format(sit))