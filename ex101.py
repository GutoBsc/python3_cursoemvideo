from datetime import datetime
def voto(ano):
    idade = datetime.now().year - ano
    if idade < 16:
        situacao = 'VOTO NEGADO'
    elif idade < 18 or idade >= 70:
        situacao = 'VOTO OPCIONAL'
    else:
        situacao = 'VOTO OBRIGATÓRIO'

    print(f'Com {idade} anos, {situacao}!')


print('-'*20)
ano_nasc = int(input('Digite o ano de nascimento: '))
voto(ano_nasc)