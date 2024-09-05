def leiaInt(texto):
    while True:
        try:
            n = int(input(texto).strip())
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m ')
            return 0
        else:
            return  n


def leiaFloat(texto):
    print(texto, end='')
    n = input().strip()
    try:
        float(n)
    except (ValueError, TypeError):
        print('\033[0;31mERRO! Digite um número real válido.\033[m ')
    except (KeyboardInterrupt):
        print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m ')
        return 0
    else:
        return n


# Programa Principal:
n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n1} e o número real {n2}')
