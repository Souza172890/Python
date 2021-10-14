from random import randint
from time import sleep
computador = randint (0,5) #esta linha faz com que o computador sorteie um número de 0 a 5
jogador = int(input('Em qual número eu pensei? ')) #nesta linha o jogador tenta adivinhar o n°
print('Processando...')
sleep(3)
if jogador == computador:
    print('Você acertou, PARABÉNS')
else:
    print('Você errou! Eu pensei no número {} e não no número {}.'.format(computador,jogador))

