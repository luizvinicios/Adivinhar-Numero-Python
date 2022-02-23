from random import randint
from time import sleep
computador = randint(0, 20)
print('Acabei de pensar em um número, será que você acerta?')
print('Dica: Foi um entre 0 e 20')
acertou= False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o número? '))
    palpite +=1
    if jogador==computador:
        acertou = True
    else:
        if jogador < computador:
            print('Maior....')
        elif jogador > computador:
            print('Menos....')
print('Analisando.....'),sleep(2)        
print('Acertou!! com {} palpites'.format(palpite))        