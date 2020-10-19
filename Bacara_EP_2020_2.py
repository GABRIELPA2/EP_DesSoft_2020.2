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
def somab(listab):
    somabanco=0
    for valor in listab: # para cada valor na lista
        somabanco+=valor # soma as duas cartas 
    if somabanco > 9:
        somabanco= somabanco-10
    # print('-----------------------------')
    # print(f'A soma do banco é {somabanco}')
    # print('-----------------------------')
    return somabanco

def somaj(listaj):
    somajogador=0
    for valor in listaj: # para cada valor na lista
        somajogador+=valor # soma as duas cartas 
    if somajogador > 9:
        somajogador= somajogador-10
    # print('-----------------------------')
    # print(f'A soma do jogador é {somajogador}')
    # print('-----------------------------')
    return somajogador

numero_cartasb=2
numero_cartasj=2
ganhador=''
A= 1
J= 0
Q= 0
K= 0
baralho= [A,2,3,4,5,6,7,8,9,10,J,Q,K]*4
baralho[9]= 0
banco=[]
jogador=[]
embaralhar=baralho[:] #Criou uma copia da lista baralho
embaralhar_cartas(embaralhar)
sortearb(embaralhar)
sortearj(embaralhar)
b=somab(banco)
j=somaj(jogador)
###
# print(f'Antes do elif b= {b} j= {j}')
if b == j:
    # print('Empate')
    ganhador='Empate'
elif b > 7 or j > 5:
    # print('Fim de jogo')
    if b > j:
        # print('O banco ganhou')
        ganhador='Banco'
    elif j > b:
        # print('O jogador ganhou')
        ganhador='Jogador'
else:
    print('Deve colocar a terceira carta')
    if j < 5:
        numero_cartasb=3
