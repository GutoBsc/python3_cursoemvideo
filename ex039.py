from datetime import date

nas = int(input('Digite o ano de seu nascimento: '))
anoat = date.today().year
idade = anoat - nas

if idade < 18:
    print('Você deverá se alistar no serviço militar em {} ano(s).'.format(18 - idade))
elif idade > 18:
    print('Você deveria ter se halistado há {} ano(s)!! Proucure suas pendências com o Governo.'.format(idade - 18))
else:
    print('Você deve se alistar esse ano!')