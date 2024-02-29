numero = input('Digite um número entre 0 e 9999: ')

lista = list(numero)
lista.reverse()
uns = lista[0]
dezs = lista[1] if len(lista) > 1 else 0
cens = lista[2] if len(lista) > 2 else 0
mils = lista[3] if len(lista) > 3 else 0
print('Resultado pelo método das strings: \n Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}'.format(uns, dezs, cens, mils))

num = int(numero)
un = num%10
dez = (num%100)// 10
cen = (num%1000) // 100
mil = (num%10000)// 1000
print('\nResultados pelo método matemático: \n Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}'.format(un, dez, cen, mil))