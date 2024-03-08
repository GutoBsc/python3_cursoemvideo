n = cont = soma = 0
print('Digite um número, e para parar digite 999:')
while True:
    n = int(input('Digite aqui: '))
    if n == 999:
        break
    cont +=1
    soma += n
print(f'Você digitou {cont} números e a soma deles é {soma}.')
