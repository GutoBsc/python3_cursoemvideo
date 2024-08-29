def leiaint(texto):
    print(texto, end='')
    v = input()
    while v.isnumeric() == False:
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[dm ')
        v= input(texto)
    return v


# Programa Principal:
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
