med = 0
cont = 0
nome_hom_velho = ''
idade_hom_vel = 0
for c in range(1,5):
    print(' --- {}ª PESSOA ---'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    med += idade
    sexo = int(input('Sexo [1 - Mac. / 2 - Fem.]: '))
    if sexo == 1:
        if idade > idade_hom_vel:
            idade_hom_vel = idade
            nome_hom_velho = nome
    elif sexo == 2:
        if idade < 20:
            cont +=1
    else:
        print('Opção de sexo inválida!')
med = med/4
print('A média de idade do grupo é de {} anos.'.format(med))
print('O homem mais velho se chama ´{}`.'.format(nome_hom_velho))
print('Nesse grupo há {} mulher(es) com menos de 20 anos.'.format(cont))