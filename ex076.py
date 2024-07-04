produtos = ('Lápis', 0.80,
            'Borracha', 3.00,
            'Caneta', 1.60,
            'Apontador', 5.00,
            'Folhas A4', 8.00,
            'Caderno Liso', 12.00,
            'Caderno Ilustrado',16.00,
            'Grifa Texto', 4.00)
print('-'*37)
print(f'{"LISTA DE PREÇOS":^37}')
print('-'*37)
for c in range (0, len(produtos)):
    if c%2 == 0:
        print(f'{produtos[c]:.<28}R${produtos[c+1]:>7.2f}')
print('-'*37)