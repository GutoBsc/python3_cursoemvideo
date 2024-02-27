import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
# hip = math.sqrt(co**2 + ca**2)
hip = math.hypot(co, ca)
print('A hipotenusa mede {:.2f}'.format(hip))