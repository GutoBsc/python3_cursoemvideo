valores = []
cont = 0
for c in range(0,5):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if c == 0:
        valores.insert(0, valor)
        print(f'O valor {valor} foi adicionado no final da lista...')
    elif c == 1:
        if valor < valores[0]:
            valores.insert(0, valor)
            print(f'O valor {valor} foi adicionado na posição 0...')
        else:
            valores.insert(1, valor)
            print(f'O valor {valor} foi adicionado no final da lista...')
    else:
        for cont, i  in enumerate(valores):
            if valor > valores[cont-1] and valor < valores[cont]:
                valores.insert(cont, valor)
                print(f'O valor {valor} foi adicionado na posição {cont}...')
        if valor > valores[len(valores)-1]:
            valores.insert(len(valores), valor)
            print(f'O valor {valor} foi adicionado na posição {len(valores)}...')
print(valores)