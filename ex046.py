from time import sleep
import emoji
print('-#-'*8)
print('Contagem regressiva...')
print('-#-'*8)
for c in range(10, -1, -1):
    print('{}...'.format(c))
    sleep(1)
print(emoji.emojize(':fireworks:')*8)
print('*   *   *   *')
print(' *   *   *   *')
print('  *   *   *   *')
print(emoji.emojize(':fireworks:')*8)