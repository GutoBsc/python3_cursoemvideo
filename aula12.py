nome = str(input('Qual o seu nome? '))
if nome == 'Augusto':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Jéssica Claudia Juliana':
    print('Belo nome feminino.')
else:
    print('Que nome sem graça.')
print('Tenha um bom dia, {}!'.format(nome))