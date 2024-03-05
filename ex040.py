n1 = float(input('Digite sua nota da P1: '))
n2 = float(input('Digite sua nota da P2: '))
med = (n1 + n2) / 2
if med < 5:
    print('Você está \033[31mreprovado\033[m!')
elif med >=5 and med <=6.9:
    print('Você está de \033[33mrecuperação\033[m, estude!')
else:
    print('Parabéns!! Você está \033[34maprovado\033[m!')