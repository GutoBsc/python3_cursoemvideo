"""dados = dict()
dados = {'nome':'Pedro', 'idade':25}
dados['sexo'] = 'M'
print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])"""

filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
         }
"""print(f'Dicionário: \n'
      f'{filme} \n'
      f'Valores: \n'
      f'{filme.values()} \n'
      f'Chaves: \n'
      f'{filme.keys()} \n'
      f'Itens: \n'
      f'{filme.items()} \n')"""

for k, v in filme.items():
    print(f'O {k} é {v}.')