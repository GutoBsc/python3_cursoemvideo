n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
n3 = int(input('Digite o terceiro número inteiro: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor número digitado foi {} e o maior {}'.format(menor, maior))

'''if n1<=n2 and n1<=n3:
    print('O menor número é o número {}'.format(n1))
elif n2<=n1 and n2<=n3:
    print('O menor número é o número {}'.format(n2))
else:
    print('O menor número é o número {}'.format(n3))
if n1>=n2 and n1>=n3:
    print('O maior número é o número {}'.format(n1))
elif n2>=n1 and n2>=n3:
    print('O maior número é o número {}'.format(n2))
else:
    print('O maior número é o número {}'.format(n3))'''