numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Dpze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis', 'Desessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número inteiro de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end='-1')
for cont, numero in enumerate(numeros):
    if cont == num:
        print(f'O número {cont} escrito por extenso é: {numero}.')