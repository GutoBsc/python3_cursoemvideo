palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in palavras:
    print(f'Na palavra {p} temos as vogais: ', end='')
    for l in p:
        if l in 'AEIOU':
            print(l.lower(), end=' ')
    print('')