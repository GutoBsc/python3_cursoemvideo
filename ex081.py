valores = []
c = 0
while True:
    valor = int(input('Digite um valor que ainda não foi adicionado ou 0 para parar: '))
    if valor == 0:
        break
    if valor not in valores:
        valores.append(valor)
    else:
        print('Valor duplicado, não vou adicionar...')
valores.sort(reverse=True)
print(f'No total foram digitados {len(valores)} valores.')
print(f' Os valores digitados em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 está presente na lista!')
else:
    print('O valor 5 não está presente na lista :(')