from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - ano_nasc
CTPS = int(input('Carteira de Trabalho (0 não tem): '))
pessoa['CTPS'] = CTPS
if CTPS != 0:
    pessoa['contratação'] = int(input('Ano da contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + 35 - (datetime.now().year['contratação'])
else:
    pessoa['contratação'] = ''
    pessoa['salário'] =''
    pessoa['aposentadoria'] = ''
print('-='*20)

for k, v in pessoa.items():
    print(f'    - {k} tem o valor {v}')