m = float(input('Digite o valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('Para {:.7f} metros temos: \n {:.6f} Kilômetros. \n {:.5f} Hectômetros. \n {:.4f} Decâmetros. \n {:.2f} Decímetros. \n {:.1f} Centímetros. \n {} Milímetros.'.format(m, km, hm, dam, dm, cm, mm))