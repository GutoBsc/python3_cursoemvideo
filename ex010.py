rs = float(input('Quantos reais você tem? R$'))
us = rs/4.98
eu = rs/5.40
yuan = rs*1.44
iene = rs*30.15
print('Com a cotação atual você consegue comprar: \n U${:.2f} \n €{:.2f} \n 元(Chi){:.2f} \n ¥(Jap){:.2f}'.format(us, eu, yuan, iene))