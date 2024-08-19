num = [2, 5, 9, 1]
num[2] = 3
num.append(7) #adiciona o número 7 no final da lista
num.sort(reverse=True) #sort() ordena e reverse=True inverte essa ordem
num.insert(2, 0) #na posição 2 da lista add o número 0
num.pop(2) #elimina o número na posição 2
num.remove(1) #elimina o elemento 1 (na primeira aparição do número 1, independente da posição)
print(num)
print(f'Essa lista tem {len(num)} elementos.')