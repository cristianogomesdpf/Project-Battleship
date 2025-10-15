'''
Implemente aqui a sua estratégia de ataque e a posição dos navios.
A estratégia de ataque deve ser implementada no método "jogar" e a posição dos navios no método "posicoes_navios".
A posição dos navios deve ser uma lista de objetos do tipo Navio, onde cada objeto contém o tamanho do navio e suas coordenadas.
A lista de navios deve conter todos os 5 navios, ou seja, um navio de tamanho 5, um de tamanho 4, dois de tamanho 3 e um de tamanho 2.

Observações:
- O tamanho dos navios é definido na constante NAVIOS, que é um dicionário onde cada chave é o nomes do navios e cada valor é o respectivo tamanho do navio.
- O tamanho do tabuleiro é definido na constante TABULEIRO_TAMANHO, que é um inteiro.
- O valor DESCONHECIDO representa uma posição vazia no tabuleiro.
- O valor NAVIO_ENCONTRADO representa uma posição onde um navio foi encontrado.
- O valor NAVIO_INTEIRO_ATINGIDO representa uma posição onde um navio foi atingido (todas as posições encontradas).
- Você pode consultar (mas não modificar) o arquivo constants.py para mais informações sobre os valores das constantes.
- Mais informações podem ser encontradas na documentação do projeto (arquivo README.md).'''

from constants import TABULEIRO_TAMANHO, NAVIOS, StatusTab
from classes._attack import Ataque
from classes._ship import Navio
from classes._pos_matriz import PosMatriz

class AlunoPlayer():
    """Classe que representa o jogador bot do aluno."""

    def __init__(self):
        """Inicializa o jogador.
        
        Atributos:
        movimentos_realizados -- Lista de movimentos já realizados pelo jogador.
        tabuleiro -- Tabuleiro do jogador (inicializado automaticamente assim que o jogo começa).
        nome -- Nome da equipe.
        """
        self.movimentos_realizados = list()
        self.tabuleiro = None           # o tabuleiro é inicializado automaticamente assim que o jogo começa
        self.nome = "{Cris & Dan}"


    def jogar(self, estado_atual_oponente, navios_afundados) -> Ataque:
        """Método para realizar uma jogada.

        Parâmetros:
        estado_atual_oponente -- O estado atual do tabuleiro.
        navios_afundados -- Lista de nomes navios afundados (em ordem de afundamento).

        Retorna um objeto do tipo Ataque com as coordenadas (x,y) da jogada.
        """

        # LÓGICA PARA ATAQUE PARA NAVIO_ENCONTRADO == True.
        direcao = ""
        for i in range(TABULEIRO_TAMANHO):
            for j in range(TABULEIRO_TAMANHO): #posição na matriz

                if self.movimentos_realizados:
                    ultimo_tiro = self.movimentos_realizados[-1]
                    ultimo_tirox, ultimo_tiroy = ultimo_tiro.x, ultimo_tiro.y
                    if estado_atual_oponente[ultimo_tirox][ultimo_tiroy] == StatusTab.NAVIO_INTEIRO_ATINGIDO.value:
                        direcao = ""
                    n, m = 0, 0
                    if estado_atual_oponente[ultimo_tirox][ultimo_tiroy] == StatusTab.NAVIO_ENCONTRADO.value and direcao == "HORIZONTAL":
                        while estado_atual_oponente((i, j + n)) == StatusTab.NAVIO_ENCONTRADO.value:
                            self.movimentos_realizados.append((i, j + n))
                            direcao = "HORIZONTAL"
                            n += 1
                            return Ataque(i, j + n)
                        while estado_atual_oponente((i, j - m)) == StatusTab.NAVIO_ENCONTRADO.value:
                            self.movimentos_realizados.append((i, j - m))
                            direcao = "HORIZONTAL"
                            m += 1
                            return Ataque(i, j - m)
                        
                    elif estado_atual_oponente[ultimo_tirox][ultimo_tiroy] == StatusTab.NAVIO_ENCONTRADO.value and direcao == "VERTICAL":
                        while estado_atual_oponente((i + n, j)) == StatusTab.NAVIO_ENCONTRADO.value:
                            self.movimentos_realizados.append((i + n, j))
                            direcao = "VERTICAL"
                            n += 1
                            return Ataque(i + n, j)
                        
                        while estado_atual_oponente((i - m, j)) == StatusTab.NAVIO_ENCONTRADO.value:
                            self.movimentos_realizados.append((i - m, j))
                            direcao = "VERTICAL"
                            m += 1
                            return Ataque(i - m, j)
                        
                if estado_atual_oponente[i][j].status == StatusTab.NAVIO_ENCONTRADO.value:
                    if direcao != "VERTICAL":   

                        # Direita (i, j + 1)
                        if j + 1 < TABULEIRO_TAMANHO:
                            if estado_atual_oponente[i][j + 1].status == StatusTab.DESCONHECIDO.value and (i, j + 1) not in self.movimentos_realizados:
                                self.movimentos_realizados.append((i, j + 1))
                                direcao = "HORIZONTAL"
                                return Ataque(i, j + 1)
                            
                        # Esquerda (i, j - 1)
                        if j - 1 >= 0:
                            if estado_atual_oponente[i][j - 1].status == StatusTab.DESCONHECIDO.value and (i, j - 1) not in self.movimentos_realizados:
                                self.movimentos_realizados.append((i, j - 1))
                                direcao = "HORIZONTAL"
                                return Ataque(i, j - 1)

                    if direcao != "HORIZONTAL":

                        # Cima (i - 1, j)
                        if i - 1 >= 0:
                            if estado_atual_oponente[i - 1][j].status == StatusTab.DESCONHECIDO.value and (i - 1, j) not in self.movimentos_realizados:
                                self.movimentos_realizados.append((i - 1, j))
                                direcao = "VERTICAL"
                                return Ataque(i - 1, j)

                        # Baixo (i + 1, j)
                        if i + 1 < TABULEIRO_TAMANHO:
                            if estado_atual_oponente[i + 1][j].status == StatusTab.DESCONHECIDO.value and (i + 1, j) not in self.movimentos_realizados:
                                self.movimentos_realizados.append((i + 1, j))
                                direcao = "VERTICAL"
                                return Ataque(i + 1, j)

        # LÓGICA DE ATAQUE PARA NAVIO_ENCONTRADO == False
        global matriz
        matriz = [[0 for i in range(10)] for i in range(10)]
        centro = 5                                      # logica: queremos começar pelo cento
        for camada in range(2, 10 + 1, 2):              #sub-matriz da 10x10 >> (2x2 até 10x10) 
            margem = camada // 2
            cima = centro - margem
            esquerda = centro - margem
            baixo = centro + margem - 1
            direita = centro + margem - 1
            #margem é a distancia do centro para a borda da matriz, cima é a linha de cima, esquerda a de baixo e assim por diante
            # matriz para ataque sem acerto - Statu == "Desconhecido"
            for i in range(cima, baixo + 1):
                for j in range(esquerda, direita + 1):
                    
                    if estado_atual_oponente[i][j].status == StatusTab.DESCONHECIDO.value and (i + j) % 2 == 0 and (i, j) not in self.movimentos_realizados: #padrão de leitura
                        self.movimentos_realizados.append((i, j))   #hist_mov

                        return Ataque(i, j) # ataque sem acerto


    def posicoes_navios(self) -> list[Navio]:
        """Determina as posições dos 5 navios no tabuleiro e retorna uma lista de objetos do tipo Navio.
        
        É preciso determinar as posições de TODOS os 5 navios, ou seja,
        um navio de tamanho 5, um de tamanho 4, dois de tamanho 3 e um de tamanho 2.
        O nome do navio será determinado automaticamente pelo tamanho do navio dentro da classe Navio."""

        """ Este posicionamento foi estratégicamente pensado para gerar mais buracos ao centro do campo de batalha.
        então a disposição segue uma ordem específica e fixada, escolhida e montada pela dupla Daniel & Cristiano.
        """
        # POSIÇÃO
        navios = []
        copia_navios = list(NAVIOS.values())
        global primeiro_tres
        primeiro_tres = True
        for tamanho in copia_navios:
            if tamanho == 5: # para 1 Carrier
                coords = [(0, 9 - k) for k in range(tamanho)]
            if tamanho == 4: # para 1 Battleship
                coords = [(2, 9 - k) for k in range(tamanho)]
            if tamanho == 3: # para 1 Cruiser (ou Submarine)
                if primeiro_tres:
                    coords = [(9, 9 - k) for k in range(tamanho)]
                    primeiro_tres = False
                else:
                    coords = [(2 - k, 0) for k in range(tamanho)] # Submarine (ou Crusier)
            if tamanho == 2:    # para 1 Destroyer
                coords = [(9 - k , 0) for k in range(tamanho)]
            navios.append(Navio(tamanho, coords))
        return navios