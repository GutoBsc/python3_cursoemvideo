n = cont = soma = 0
print('Digite um número, e para parar digite 999:')
while n != 999:
    n = int(input('Digite aqui: '))
    if n != 999:
        cont +=1
        soma += n
print('Você digitou {} números e a soma deles é {}.'.format(cont, soma))
