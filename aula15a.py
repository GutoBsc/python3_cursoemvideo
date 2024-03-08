n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma é {}'.format(s))  -> PYTHON 3
print(f'A soma é {s}') #PYTHON 3.6 +
