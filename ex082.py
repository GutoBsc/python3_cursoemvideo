valores = []
pares =[]
impares = []
c = 0
while True:
    valor = int(input('Digite um valor que ainda não foi adicionado ou 0 para parar: '))
    if valor == 0:
        break
    if valor not in valores:
        valores.append(valor)
    else:
        print('Valor duplicado, não vou adicionar...')
valores.sort()
print(f' Os valores digitados em ordem decrescente são: {valores}')
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Os valores pares são: {pares}')
print(f'Os valores impares são: {impares}')