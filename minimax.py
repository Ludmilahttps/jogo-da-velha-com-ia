def checar_vitoria(tabuleiro, marcador):
    return (
        (tabuleiro[1] == marcador and tabuleiro[2] == marcador and tabuleiro[3] == marcador) or
        (tabuleiro[4] == marcador and tabuleiro[5] == marcador and tabuleiro[6] == marcador) or
        (tabuleiro[7] == marcador and tabuleiro[8] == marcador and tabuleiro[9] == marcador) or
        (tabuleiro[1] == marcador and tabuleiro[4] == marcador and tabuleiro[7] == marcador) or
        (tabuleiro[2] == marcador and tabuleiro[5] == marcador and tabuleiro[8] == marcador) or
        (tabuleiro[3] == marcador and tabuleiro[6] == marcador and tabuleiro[9] == marcador) or
        (tabuleiro[1] == marcador and tabuleiro[5] == marcador and tabuleiro[9] == marcador) or
        (tabuleiro[7] == marcador and tabuleiro[5] == marcador and tabuleiro[3] == marcador)
    )

def checagem_empate(tabuleiro):
    for i in range(1, 10):
        if tabuleiro[i] == ' ':
            return False
    return True

def minimax(tabuleiro, e_maximizador, jogador_1, jogador_2):
    if checar_vitoria(tabuleiro, jogador_2):
        return (None, 1)
    elif checar_vitoria(tabuleiro, jogador_1):
        return (None, -1)
    elif checagem_empate(tabuleiro):
        return (None, 0)

    if e_maximizador:
        melhor_pontuacao = -float('inf')
        melhor_movimento = None
        for posicao in range(1, 10):
            if tabuleiro[posicao] == ' ':
                tabuleiro[posicao] = jogador_2
                _, pontuacao = minimax(tabuleiro, False, jogador_1, jogador_2)
                tabuleiro[posicao] = ' '
                if pontuacao > melhor_pontuacao:
                    melhor_pontuacao = pontuacao
                    melhor_movimento = posicao
        return melhor_movimento, melhor_pontuacao
    else:
        melhor_pontuacao = float('inf')
        melhor_movimento = None
        for posicao in range(1, 10):
            if tabuleiro[posicao] == ' ':
                tabuleiro[posicao] = jogador_1
                _, pontuacao = minimax(tabuleiro, True, jogador_1, jogador_2)
                tabuleiro[posicao] = ' '
                if pontuacao < melhor_pontuacao:
                    melhor_pontuacao = pontuacao
                    melhor_movimento = posicao
        return melhor_movimento, melhor_pontuacao
