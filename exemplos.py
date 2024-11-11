#exemplos de uso

from jogovelha import JogoVelha, Tabuleiro, JogadorHumano, JogadorComputador

pietro = JogadorHumano("Pietro")
robozao_do_mal = JogadorComputador("Robozin", "aleatoria")
jogo_da_velha = JogoVelha(pietro, robozao_do_mal)
jogo_da_velha.jogar()