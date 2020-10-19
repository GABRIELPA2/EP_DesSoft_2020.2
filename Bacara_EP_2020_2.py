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
print('-'*30)
print('Jogo Bacara')
print('-'*30)
print('')
play= str(input('Vamos começar?[S/N] ')).upper()

if play[0] != 'N':
#############Comprar Fichas###################
    fichas=0
    escolha= 0
    a=0
    while escolha != 6:
        time.sleep(1)
        escolha= int(input("""
    ======================
    Escolha uma das opções 
    ======================\n
    [1] 100 Fichas (R$ 200)
    [2] 200 Fichas (R$ 400)
    [3] 300 Fichas (R$ 600)
    [4] 400 Fichas (R$ 800)
    [5] 500 Fichas (R$ 1000)
    [6] Não quero mais jogar
    Escolha: """))
        if escolha == 1:
            fichas= 100
            print('')
            print('Fichas compradas com sucesso, bom jogo!')
            print(f'    ===Nota Fiscal=== \n Compra______ {fichas} fichas \n Valor______ 200 reais')
            break
        elif escolha == 2:
            fichas= 200
            print('')
            print('Fichas compradas com sucesso, bom jogo!')
            print(f'    ===Nota Fiscal=== \n Compra______ {fichas} fichas \n Valor______ 400 reais')
            break
        elif escolha == 3:
            fichas= 300
            print('')
            print('Fichas compradas com sucesso, bom jogo!')
            print(f'    ===Nota Fiscal=== \n Compra______ {fichas} fichas \n Valor______ 600 reais')
            break
        elif escolha == 4:
            fichas= 400
            print('')
            print('Fichas compradas com sucesso, bom jogo!')
            print(f'    ===Nota Fiscal=== \n Compra______ {fichas} fichas \n Valor______ 800 reais')
            break
        elif escolha == 5:
            fichas= 500
            print('')
            print('Fichas compradas com sucesso, bom jogo!')
            print(f'    ===Nota Fiscal=== \n Compra______ {fichas} fichas \n Valor______ 1000 reais')
            break
        elif escolha == 6:
            a= 1
            print('')
            print('Tchau!')
            break
        else:
            print("Valor invalido tente novamenete")
else:
    a=1
    fichas=0
    print('Ok, podemos jogar depois')
##########################################################
while fichas > 0:
    valor_apostado= int(input('Quantas fichas deseja apostar: '))
    aposta=''
    opcao=0
    while opcao != 3:
        escolha= int(input("""
    ======================
    Escolha uma das opções 
    ======================\n
    [1] Apostar no Banco
    [2] Apostar no Jogador
    [3] Apostar no Empate
    Escolha: """))
        
        if escolha == 1:
            aposta=('Banco')
            print('Carregando......')
            time.sleep(2)
            print(f'Ok, suas apostas serão direcionadas ao {aposta} \n')
            time.sleep(2)
            print('==========================')
            print(f'A cartas do banco foram : {banco}')
            print(f'A soma das cartas do banco foi: {b}')
            print(f'A cartas do jogador foram : {jogador}')
            print(f'A soma das jogador do banco foi: {j}')
            print('========================== \n')
            if aposta==ganhador:
                print(f'Vc apostou no {aposta} e ganhou')
                valor=  math.trunc(valor_apostado*0.95)
                fichas= fichas + valor
                print(f'Vc ganhou {valor} fichas, agr vc tem {fichas} fichas')
                comisao= fichas*0.00106 ####Commisao
                fichas= fichas - comisao
            else:
                print(f'Vc apostou no {aposta} e deu {ganhador}, vc perdeu!')
                fichas= fichas - valor_apostado
                print(f'Vc perdeu {valor_apostado} fichas, agr vc tem {fichas} fichas')
            break
        
        elif escolha == 2:
            aposta=('Jogador')
            print('Carregando......')
            time.sleep(2)
            print(f'Ok, suas apostas serão direcionadas ao {aposta} \n')
            time.sleep(2)
            print('==========================')
            print(f'A cartas do banco foram : {banco}')
            print(f'A soma das cartas do banco foi: {b}')
            print(f'A cartas do jogador foram : {jogador}')
            print(f'A soma das jogador do banco foi: {j}')
            print('========================== \n')
            if aposta==ganhador:
                print(f'Vc apostou no {aposta} e ganhou')
                fichas= fichas + valor_apostado
                comisao= fichas*0.00124 ####Commisao
                fichas= fichas - comisao
            else:
                print(f'Vc apostou no {aposta} e deu {ganhador}, vc perdeu!')
                fichas= fichas - valor_apostado
                print(f'Vc perdeu {valor_apostado} fichas, agr vc tem {fichas} fichas')
            break
        
        elif escolha == 3:
            aposta=('Empate')
            print('Carregando......')
            time.sleep(2)
            print(f'Ok, suas apostas serão direcionadas ao {aposta} \n')
            time.sleep(2)
            print('==========================')
            print(f'A cartas do banco foram : {banco}')
            print(f'A soma das cartas do banco foi: {b}')
            print(f'A cartas do jogador foram : {jogador}')
            print(f'A soma das jogador do banco foi: {j}')
            print('========================== \n')
            if aposta==ganhador:
                print(f'Vc apostou no {aposta} e ganhou')
                valor= valor_apostado*8
                fichas= fichas + valor
                comisao= fichas*1.44 ####Commisao
                fichas= fichas - comisao
                print(f'Vc ganhou {valor} fichas, agr vc tem {fichas} fichas')
                
            else:
                print(f'Vc apostou no {aposta} e deu {ganhador}, vc perdeu!')
                fichas= fichas - valor_apostado
                print(f'Vc perdeu {valor_apostado} fichas, agr vc tem {fichas} fichas')
            break
        else:
            print('Valor invalido, vamos tentar novamete')
    if fichas == 0:
        print('====================')
        print('Vc perdeu tudo!!!')
        print('Sorte no amor e azar no jogo? Ou azar nos dois?')
        print('Mais sorte da proxima vez! Tchau!')
        print('====================')
        break
    else:
        jog= input('Deseja continuar jogando? ').upper()
        if jog[0] == 'N':
            print('====================')
            print('Obrigado por jogar!')
            print('====================')
            print('')
            print(f'Voçê terminou com {fichas} fichas')
            print(f'Voçê ficou com R$ {fichas*2} reais')
            break
        else:
            print('Vamos continuar')
