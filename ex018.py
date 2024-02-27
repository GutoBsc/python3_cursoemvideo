from math import radians, sin, cos, tan
ang = float(input('Digite o angulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))
print('Os valores de seno, cosseno e tangente são: \n Seno = {:.2f} \n Cosseno = {:.2f} \n Tangente = {:.2f}'.format(sen, cos, tg))