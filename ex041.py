from datetime import date
nas = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = ano_atual - nas

if idade <= 9:
    categoria = 'mirim'
elif idade <= 14:
    categoria = 'infantil'
elif idade <= 19:
    categoria = 'junior'
elif idade <= 25:
    categoria = 'senior'
else:
    categoria = 'master'
print('A categoria do atleta é \033[1;35m{}\033[m.'.format(categoria))