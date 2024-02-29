frase = 'Curso em Vídeo Python'
print(frase[:14])
print(frase[15:])
print(frase.count('o'))
print(len(frase))

frase = frase.replace('Python', 'JavaScript')
print(frase)
print(len(frase))
print('Java' in frase)
print(frase.find('Java'))