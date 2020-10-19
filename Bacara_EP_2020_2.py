import random
import math
import time

def embaralhar_cartas(cartas):
    random.shuffle(embaralhar) #Embaralhou aleatoriamente a lista
    # print(embaralhar)

def sortearb(cartas):
    for c in range(0,numero_cartasb):
        cartabanco= random.choice(cartas) #Escolheu aleatoriamente uma carta da lista
        banco.append(cartabanco)
        cartas.remove(cartabanco) #Removeu a carta do baralho
    #     print('-----------------------------')
    #     print(f'A carta {c+1} do banco é {cartabanco}')
    #     print('-----------------------------')
    # print(cartas)
    # print(len(cartas))
    # print(f'A lista do banco é {banco}')
def sortearj(cartas):
    for c in range(0,numero_cartasj):
        cartajogador= random.choice(cartas) #Escolheu aleatoriamente uma carta da lista
        jogador.append(cartajogador)
        cartas.remove(cartajogador) #Removeu a carta do baralho
    #     print('-----------------------------')
    #     print(f'A carta {c+1} do jogador é {cartajogador}')
    #     print('-----------------------------')
    # print(cartas)
    # print(len(cartas))
    # print(f'A lista do jogador é {jogador}')
