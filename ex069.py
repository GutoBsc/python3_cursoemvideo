mais_dezoito = 0
homens = 0
mulher_menos_vinte = 0
n = 1
while True:
    print(f' --- {n}ª PESSOA ---')
    n += 1
    idade = int(input('Idade: '))
    sexo = int(input('Sexo [1 - Mac. / 2 - Fem.]: '))
    if idade > 18:
        mais_dezoito += 1
    if sexo == 1:
        homens += 1
    elif sexo == 2:
        if idade < 20:
            mulher_menos_vinte += 1
    else:
        print('Opção de sexo inválida!')
    while True:
        cont = str(input('Você quer continuar? [S/N]')).upper()
        if cont not in 'SN':
            break
    if cont == 'N':
        break
print(f'Nesse grupo há {mais_dezoito} pessoas com mais de 18 anos.')
print(f'Nesse grupo há {homens} homens')
print(f'Nesse grupo há {mulher_menos_vinte} mulher(es) com menos de 20 anos.')