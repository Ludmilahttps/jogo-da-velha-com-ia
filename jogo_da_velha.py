import random
import os
from minimax import checar_vitoria, checagem_empate, minimax

def printar_tabuleiro(tabuleiro):
    print('     |     |       ')
    print(f'  {tabuleiro[1]}  |  {tabuleiro[2]}  |  {tabuleiro[3]}')
    print('     |     |       ')
    print('------------------')
    print('     |     |       ')
    print(f'  {tabuleiro[4]}  |  {tabuleiro[5]}  |  {tabuleiro[6]}')
    print('     |     |       ')
    print('------------------')
    print('     |     |       ')
    print(f'  {tabuleiro[7]}  |  {tabuleiro[8]}  |  {tabuleiro[9]}')
    print('     |     |       ')

def escolher_marcador():
    marcador = ''
    while not (marcador == 'X' or marcador == 'O'):
        marcador = input('Player 1: Você quer ser X ou O? ').upper()

    if marcador == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def marcar_posicao(tabuleiro, marcador, posicao):
    tabuleiro[posicao] = marcador

def primeiro_jogar():
    if random.randint(0, 1) == 0:
        return 'Jogador 1'
    else:
        return 'Jogador 2'

def checar_espaco(tabuleiro, posicao):
    return tabuleiro[posicao] == ' '

def escolha_jogada(tabuleiro, jogador):
    posicao = ' '
    while posicao not in '1 2 3 4 5 6 7 8 9'.split() or not checar_espaco(tabuleiro, int(posicao)):
        posicao = input(f'{jogador} - escolha sua jogada entre 1-9: ')
    return int(posicao)

def replay():
    return input('Você quer jogar novamente? SIM ou NÃO? ').lower().startswith('s')

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Bem vindo ao jogo da velha!')

        tabuleiro = [' '] * 10
        jogador_1, jogador_2 = escolher_marcador()
        turno_jogador = primeiro_jogar()
        print(turno_jogador, 'começa!')
        status_jogo = True

        while status_jogo:
            if turno_jogador == 'Jogador 1':
                printar_tabuleiro(tabuleiro)
                posicao_jogada = escolha_jogada(tabuleiro, turno_jogador)
                marcar_posicao(tabuleiro, jogador_1, posicao_jogada)

                if checar_vitoria(tabuleiro, jogador_1):
                    printar_tabuleiro(tabuleiro)
                    print("Parabéns, você ganhou a partida!")
                    status_jogo = False
                else:
                    if checagem_empate(tabuleiro):
                        printar_tabuleiro(tabuleiro)
                        print("O jogo empatou!")
                        break
                    else:
                        turno_jogador = 'Jogador 2'

            else:
                # IA faz seu movimento
                printar_tabuleiro(tabuleiro)
                print("Vez do Jogador 2 (IA)...")

                movimento, _ = minimax(tabuleiro, True, jogador_1, jogador_2)
                marcar_posicao(tabuleiro, jogador_2, movimento)

                if checar_vitoria(tabuleiro, jogador_2):
                    printar_tabuleiro(tabuleiro)
                    print("Jogador 2 (IA) venceu!")
                    status_jogo = False
                else:
                    if checagem_empate(tabuleiro):
                        printar_tabuleiro(tabuleiro)
                        print("O jogo empatou!")
                        break
                    else:
                        turno_jogador = 'Jogador 1'

        if not replay():
            break
