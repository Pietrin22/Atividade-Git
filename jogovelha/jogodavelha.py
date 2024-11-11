#importando metódos de bibliotecas nativas
from abc import ABC, abstractmethod
from random import choice
from typing import Optional, Tuple

class JogoVelha:
     def __init__(self, jogador1: "Jogador" , jogador2: "Jogador") -> None:
         """Inicializa um JogoVelha com lista de jogadores, cria um tabuleiro e define turno e símbolos dos jogadores.

         Args:
             jogador1(Jogador): primeiro Jogador do JogoVelha.
             jogador2(Jogador): Segundo Jogador do JogoVelha.
         """
         self.jogadores = [jogador1, jogador2]
         self.tabuleiro = Tabuleiro()
         self.turno = 1
         jogador1.simbolo = "X"
         jogador2.simbolo = "O"

     def jogar(self) -> None:
         """Roda a mecânica do Jogo usando todas as funções.

         A função define um looping , que vai rodar até ser identificado
         uma condição de vitória ou empate, ela verifica o jogador atual
         e pede para ele fazer sua jogada, marca a jogada no tabuleiro,
         imprime o tabuleiro passa o turno para o próximo jogador e volta ao ínicio.
         """
         while True:
             jogador_atual = self.jogador_atual()
             self.jogador_atual()
             jogada = jogador_atual.fazer_jogada(self.tabuleiro)
             self.tabuleiro.marcar_casa(jogada, jogador_atual.simbolo)
             self.tabuleiro.imprimir_tabuleiro()
             if self.turno == 1:
                 self.turno = 2
             elif self.turno == 2:
                 self.turno = 1
             if self.checar_fim_de_jogo() != None:
                 print(f"O jogo acabou pois houve um(a) {self.checar_fim_de_jogo()}")
                 break

     def checar_fim_de_jogo(self) -> Optional[str]:
         """Checa as condições de fim de jogo (vitória ou empate).

         Returns:
             Optional[str]: se o jogo acabou retorna a razão para ter acabado.
        """
        #verificando se alguém completou uma linha e retornando a vitória.
         for linha in self.tabuleiro.casas:
             if linha == [["X"], ["X"], ["X"]]:
                 return f"Vitória do {self.jogadores[0].nome}"
             elif linha == [["O"], ["O"], ["O"]]:
                 return f"vitória do {self.jogadores[1].nome}"
         #verificando se alguém completou uma diagonal e retornando a vitória.
         if self.tabuleiro.casas[0][0] == self.tabuleiro.casas[1][1] == self.tabuleiro.casas[2][2] == ["X"]:
             return f"vitória do {self.jogadores[0].nome}"
         elif  self.tabuleiro.casas[0][0] == self.tabuleiro.casas[1][1] == self.tabuleiro.casas[2][2] == ["O"]:
             return f"vitória do {self.jogadores[1].nome}"
         elif self.tabuleiro.casas[0][2] == self.tabuleiro.casas[1][1] == self.tabuleiro.casas[2][0] == ["X"]:
             return f"vitória do {self.jogadores[0].nome}"
         elif self.tabuleiro.casas[0][2] == self.tabuleiro.casas[1][1] == self.tabuleiro.casas[2][0] == ["O"]:
             return f"vitória do {self.jogadores[1].nome}"
         #verificando se alguém marcou uma coluna e retornando a vitória.
         elif self.tabuleiro.casas[0][0] == self.tabuleiro.casas[1][0] == self.tabuleiro.casas[2][0] == ["X"]:
             return f"vitória do {self.jogadores[0].nome}"
         elif self.tabuleiro.casas[0][0] == self.tabuleiro.casas[1][0] == self.tabuleiro.casas[2][0] == ["O"]:
             return f"vitória do {self.jogadores[1].nome}"
         elif self.tabuleiro.casas[0][1] == self.tabuleiro.casas[1][1] == self.tabuleiro.casas[2][1] == ["X"]:
             return f"vitória do {self.jogadores[0].nome}"
         elif self.tabuleiro.casas[0][1] == self.tabuleiro.casas[1][1] == self.tabuleiro.casas[2][1] == ["O"]:
             return f"vitória do {self.jogadores[1].nome}"
         elif self.tabuleiro.casas[0][2] == self.tabuleiro.casas[1][2] == self.tabuleiro.casas[2][2] == ["X"]:
             return f"vitória do {self.jogadores[0].nome}"
         elif self.tabuleiro.casas[0][2] == self.tabuleiro.casas[1][2] == self.tabuleiro.casas[2][2] == ["O"]:
             return f"vitória do {self.jogadores[1].nome}"
         #verificando se houve um empate, ou seja não há casas vazia e retornando o empate.
         elif [] not in self.tabuleiro.casas[0] and [] not in self.tabuleiro.casas[1] and [] not in self.tabuleiro.casas[2]:
             return "empate"

     def jogador_atual(self) -> "Jogador":
         """Verifica quem é o jogador atual, checando o turno e retorna-o.

         Returns:
             Jogador: retorna o Jogador que vai jogar (Jogador atual).
         """
         if self.turno == 1:
             return self.jogadores[0]
         elif self.turno == 2:
             return self.jogadores[1]


class Tabuleiro:
    def __init__(self) -> None:
        """Inicializa um tabuleiro com casas vazias.
        """
        self.casas = [[[], [], []], [[], [], [],], [[], [], []]]

    def pegar_tabuleiro(self) -> list[list]:
        """Retorna as casas do tabuleiro.

        Returns:
            list[list]: retorna as casas do tabuleiro.
        """
        return self.casas

    def marcar_casa(self, pos: Tuple[int,int], valor: str) -> None:
        """Verifica se a casa (int, int) do tabuleiro está vazia e adiciona o valor nela.

        Args:
            pos(Tuple[int,int]): Index da casa que deve ser marcada.
            valor(str): símbolo do Jogador para ser marcado na casa.
        """
        if self.casas[pos[0]][pos[1]] == []:
            self.casas[pos[0]][pos[1]] = [valor]

    def imprimir_tabuleiro(self) -> None:
        """Imprime o tabuleiro linha a linha.
        """
        for linha in self.casas:
            print(linha)


class Jogador(ABC):
    #simbolo do jogador que vai ser definido com "X" ou "O" pela classe JogoVelha
    simbolo = " "
    def __init__(self, nome: str) -> None:
        """Inicializa um jogador com nome.

        Args:
            nome(str): nome do Jogador.
        """
        self.nome = nome

    #metódo vazio que deve ser mudado pelas outras classes
    @abstractmethod
    def fazer_jogada(self, tabuleiro: Tabuleiro) -> Tuple[int,int]:
        """Não faz nada, subclasses devem adicionar alguma coisa.
        """
        pass


class JogadorHumano(Jogador):
#herda o __init__ da superclasse Jogador
    def fazer_jogada(self, tabuleiro: Tabuleiro) -> Tuple[int,int]:
        """imprime o nome do Jogador, define um looping para pedir a jogada e retorna-a em forma de Tupla.

        Args:
            tabuleiro(Tabuleiro): tabuleiro em que a jogada será feita.

        Returns:
            Tuple[int, int]: retorna as posições de linha e coluna para marcar.

        Raises:
            ValueError: quando o x ou y não têm somente números, pois um Index precisa ser um número.
            IndexError: quando o x ou y são números diferentes de 0,1 e 2, pois só têm esses Index no Tabuleiro.
        """
        print(f"O jogador {self.nome} irá jogar")
        while True:
            try:
                x = int(input("Em qual linha gostarias de jogar? (de 0 a 2)"))
                y = int(input("Em qual coluna gostarias de jogar? (de 0 a 2)"))
                if not tabuleiro.casas[x][y] == []:
                    print("Houve um erro, você não pode escolher uma casa já ocupada!!")
                else:
                    break
            except ValueError:
                print("Houve um erro, você deve digitar um número!!")
            except IndexError:
                print("Houve um erro, o número deve ser entre um inteiro entre 0 e 2!!")
        return (x,y)


class JogadorComputador(Jogador):
    #lista para ser escolhida uma coordenada aleatoriamente
    lista_escolhas_xy = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    def __init__(self, nome: str, estrategia: str) -> None:
        """Inicializa um JogadorComputador com nome e estrategia, se a estrategia não estiver definida força ValueError.

        Args:
            nome(str): nome do JogadorComputador
            estrategia(str): estrategia que ele vai seguir (somente aleátoria).

        Raises:
            ValueError: Quando a estratégia não é "aleatoria", pois só estratégia "aleatoria" está definida.
        """
        if estrategia == "aleatoria":
            self.nome = nome
            self.estrategia = estrategia
        else:
            raise ValueError("estratégia inválida tente novamente")

    def fazer_jogada(self, tabuleiro: Tabuleiro) -> Tuple[int,int]:
        """imprime o nome do Jogador, verifica se a estratégia é "aleatoria" e sorteia uma coordenada da lista de escolhas.

        Args:
            tabuleiro(Tabuleiro): Tabuleiro em que a jogada será feita.

        Returns:
            Tuple[int, int]: retorna a linha e a coluna que será marcada.
        """
        if self.estrategia == "aleatoria":
            print(f"O jogador {self.nome} irá jogar")
            while True:
                coord_xy = choice(self.lista_escolhas_xy)
                #verificando se a casa está vazia e se sim quebra o looping
                if tabuleiro.casas[coord_xy[0]][coord_xy[1]] == []:
                    break
                #se estiver com um símbolo apaga a coordena da lista_escolhas_xy
                else:
                    del self.lista_escolhas_xy[self.lista_escolhas_xy.index(coord_xy)]
            del self.lista_escolhas_xy[self.lista_escolhas_xy.index(coord_xy)]
            return coord_xy
