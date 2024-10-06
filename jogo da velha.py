from random import randrange
from os import system,name
from time import sleep

def derrota():
    if escolhaMultijogador == 1:
        print("Voce perdeu")
    elif escolhaMultijogador == 2:
        print("Adversário, voce ganhou!!!")
    x = input('aperte qualquer ENTER para sair')

def vitoria():
    print('Jogador 1, voce ganhou!!!')
    x = input('aperte qualquer ENTER para sair')

def clear():
    system('cls' if name == 'nt' else 'clear')

tabu2 =[1, 2, 3, 4, 5, 6, 7, 8, 9]
tabu = tabu2


while(True):  #escolha do usuário para modo de jogo
    escolhaMultijogador = int(input("Qual modo gostaria de jogar? \n1-singleplayer  2-multiplayer"))
    if escolhaMultijogador == 1 or 2:
        break
    else:
        print("algo está errado, reiniciando...")
        sleep(2)
        clear()

while True:
    clear()   #ascii do jogo da velha(parte mais dificil)
    print('+-------+-------+-------+'
          '\n|       |       |       |'
          '\n|   {}   |   {}   |   {}   |'
          '\n|       |       |       |'
          '\n+-------+-------+-------+'
          '\n|       |       |       |'
          '\n|   {}   |   {}   |   {}   |'
          '\n|       |       |       |'
          '\n+-------+-------+-------+'
          '\n|       |       |       |'
          '\n|   {}   |   {}   |   {}   |'
          '\n|       |       |       |'
          '\n+-------+-------+-------+'.format(tabu[0], tabu[1], tabu[2], tabu[3], tabu[4], tabu[5], tabu[6], tabu[7], tabu[8]))
    esco = int(input('(Jogador)Qual seria a sua jogada? '))

    #verificação para a pessoa não escolher um numero ocupado
    while True:
        if tabu[esco - 1] == 'O' or tabu[esco - 1] == 'X':
            esco = int(input('Esse já ta ocupado! '))
            continue
        else:
            tabu[esco - 1] = 'X'
            break
        
    # verificação e requisição ao player 2/máquina para a jogada do adversário
    while True:
        if escolhaMultijogador == 1:
            escov = randrange(1, 9)
        elif escolhaMultijogador == 2:
            escov = int(input("(Adversário)Qual é a sua jogada?"))
        if tabu[escov - 1] == 'X' or tabu[escov - 1] == 'O':
            if escolhaMultijogador == 2:
                print("Essa ta ocupado!!!")
            continue
        else:
            tabu[escov - 1] = 'O'
            break

    # analise vitória do player 1
    if tabu[0] == 'X' and tabu[1] == 'X' and tabu[2] == 'X':
        vitoria()
        break
    elif tabu[3] == 'X' and tabu[4] == 'X' and tabu[5] == 'X':
        vitoria()
        break
    elif tabu[6] == 'X' and tabu[7] == 'X' and tabu[8] == 'X':
        vitoria()
        break
    elif tabu[0] == 'X' and tabu[3] == 'X' and tabu[6] == 'X':
        vitoria()
        break
    elif tabu[1] == 'X' and tabu[4] == 'X' and tabu[7] == 'X':
        vitoria()
        break
    elif tabu[2] == 'X' and tabu[5] == 'X' and tabu[8] == 'X':
        vitoria()
        break
    elif tabu[0] == 'X' and tabu[4] == 'X' and tabu[8] == 'X':
        vitoria()
        break
    elif tabu[2] == 'X' and tabu[4] == 'X' and tabu[6] == 'X':
        vitoria()
        break

    # analise do player 2/máquina
    elif tabu[0] == 'O' and tabu[1] == 'O' and tabu[2] == 'O':
        derrota()
        break
    elif tabu[3] == 'O' and tabu[4] == 'O' and tabu[5] == 'O':
        derrota()
        break
    elif tabu[6] == 'O' and tabu[7] == 'O' and tabu[8] == 'O':
        derrota()
        break
    elif tabu[0] == 'O' and tabu[3] == 'O' and tabu[6] == 'O':
        derrota()
        break
    elif tabu[1] == 'O' and tabu[4] == 'O' and tabu[7] == 'O':
        derrota()
        break
    elif tabu[2] == 'O' and tabu[5] == 'O' and tabu[8] == 'O':
        derrota()
        break
    elif tabu[0] == 'O' and tabu[4] == 'O' and tabu[8] == 'O':
        derrota()
        break
    elif tabu[2] == 'O' and tabu[4] == 'O' and tabu[6] == 'O':
        derrota()
        break
