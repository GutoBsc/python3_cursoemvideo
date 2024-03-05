from datetime import date
ano_at = date.today().year
cont = 0
for c in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if (ano_at - ano) >= 21:
        cont += 1
print('Deesas pessoas, {} delas são maiores de idade.'.format(cont))
