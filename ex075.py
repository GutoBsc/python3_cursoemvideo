valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print('-'*20)
print(f'O valor 9 apareceu {valores.count(9)} vez(es).')
print('-'*20)
if valores.count(3) > 0:
    print(f'O valor 3 foi digitado pela primeira vez na {valores.index(3)+1}ª posição.')
else:
    print('O valor 3 não apareceu nenhuma vez.')
print('-'*20)
print('Os valores pares são: ')
for c in valores:
    if (c%2 == 0):
        print(c)