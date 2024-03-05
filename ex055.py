maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Dentre essas pessoas, a de maior peso possui {}Kg, e a de menor {}Kg.'.format(maior, menor))
