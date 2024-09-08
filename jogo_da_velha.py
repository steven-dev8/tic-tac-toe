from random import choice, uniform
from time import sleep

def linha():
    print('-=' * 16)

def jogo():
    linha()
    print(f'{' 0   1   2': >20}')

    for i, j in enumerate(game):
        if i == 0:
            print(f'{f'A  {j[0]} | {j[1]} | {j[2]}': >20}')
        elif i == 2:
            print(f'{f'C  {j[0]} | {j[1]} | {j[2]}': >20}')
        else:
            print(f'{f'  {'-'*11}': >21}')
            print(f'{f'B  {j[0]} | {j[1]} | {j[2]}': >20}')
            print(f'{f'  {'-'*11}': >21}')
    linha()

def valid():
    global posicao
    while posicao not in VALID:
        posicao = input('Digite uma posição valida: ')
    VALID.remove(posicao)
    return posicao, True

def converter(posicao):
    linha = posicao[0]
    coluna = int(posicao[1])
    if linha == 'A':
        linha = 0
    elif linha == 'B':
        linha = 1
    elif linha == 'C':
        linha = 2
    return [linha, coluna]

def pensando():
    jogo()
    tempo_bot = uniform(1, 3)
    print('Pensando...')
    sleep(tempo_bot)

game = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

print(f'{'JOGO DA VELHA': >22}')
jogo()

LADO = None
while LADO not in ['1','2']:
    print('ESCREVA NESSE FORMATO LxC. Ex: A1')

    LADO = input(f'LADOS\n'
                'X - 1\n'
                'O - 2\n'
                'ESCOLHA UM LADO: ')
    
    if LADO == '1' or LADO == '2':
        if LADO == '1':
            LADO1 = 'X'
            LADO2 = 'O'
        else:
            LADO2 = 'X'
            LADO1 = 'O'
        break

VALID = ['A0', 'A1', 'A2', 'B0','B1','B2','C0','C1','C2']
JOGADOR = True
CONTINUAR = True

while True:
    if len(VALID) == 0:
        jogo()
        print('DEU VELHA!!!')
        break

    for i in game:
        if i[0] == i[1] == i[2] and i[0] != ' ':
            jogo()
            print(f'O jogador "{i[0]}" GANHOU!!!')
            CONTINUAR = False
            break

    if game[0][0] == game[1][0] == game[2][0] and game[0][0] != ' ':
        jogo()
        print(f'O jogador "{game[0][0]}" GANHOU!!!')
        break
    elif game[0][1] == game[1][1] == game[2][1] and game[0][1] != ' ':
        jogo()
        print(f'O jogador "{game[0][1]}" GANHOU!!!')
        break
    elif game[0][2] == game[1][2] == game[2][2] and game[0][2] != ' ':
        jogo()
        print(f'O jogador "{game[0][2]}" GANHOU!!!')
        break
    elif game[0][0] == game[1][1] == game[2][2] and game[1][1] != ' ':
        jogo()
        print(f'O jogador "{game[1][1]}" GANHOU!!!')
        break
    elif game[2][0] == game[1][1] == game[0][2] and game[1][1] != ' ':
        jogo()
        print(f'O jogador "{game[1][1]}" GANHOU!!!')
        break

    if CONTINUAR:
        if JOGADOR:
            jogo()
            posicao = input('Digite a posição: ')

            if valid():
                posicao = converter(posicao)
                game[posicao[0]][posicao[1]] = LADO1
                JOGADOR = False

        elif JOGADOR == False:
            pensando()
            posicao = choice(VALID)
            valid()
            posicao = converter(posicao)
            game[posicao[0]][posicao[1]] = LADO2
            JOGADOR = True
    else:
        break

print('FIM')
sleep(2)