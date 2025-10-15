
# Batalha Naval

**Batalha Naval** (tamb�m conhecida como *Battleships*) � um jogo de adivinha��o estrat�gica para dois jogadores. � jogado em grades marcadas (em papel ou tabuleiro), nas quais cada jogador posiciona sua frota de navios de guerra. **As posi��es dos navios do advers�rio s�o mantidas ocultas**. Os jogadores se revezam efetuando "disparos" no tabuleiro do oponente e o objetivo � destruir completamente a frota advers�ria, ou seja, afundar todos os seus navios. O jogo termina quando um dos jogadores afunda toda a frota inimiga.

Seguiremos como base as regras do jogo da Hasbro, dispon�veis em [https://www.hasbro.com/common/instruct/battleship.pdf](https://www.hasbro.com/common/instruct/battleship.pdf), com algumas modifica��es para facilitar a implementa��o, conforme descrito abaixo.

## Objetivo do Projeto

Neste projeto da disciplina **MC102**, voc� dever� desenvolver uma **estrat�gia de ataque** para o jogo Batalha Naval, que envolver�:

- Um algoritmo para **definir as posi��es dos seus navios**. Este algoritmo ser� executado **apenas uma vez**, no in�cio do jogo. 
  - *Aten��o*: Seus navios n�o podem ser sobrepostos e nem posicionados fora dos limites do mapa. E devem ser posicionados horizontal ou verticalmente.
- Um algoritmo para **atacar os navios do oponente**, que deve buscar maximizar as chances de acerto. Este algoritmo ser� executado a **cada rodada**, ou seja, a cada disparo realizado.
  - *Aten��o*: Caso voc� ataque uma posi��o mais de uma vez, o jogo continua, mas voc� perde a jogada, isto �, perde a chance de acertar um navio. Portanto, � importante que voc� tenha um controle das posi��es j� atacadas.

O jogo acontece em um tabuleiro **10x10**, e cada jogador disp�e de **5 navios**, distribu�dos conforme os tamanhos a seguir:
- 1 navio de tamanho 5, o "Carrier"
- 1 navio de tamanho 4, o "Battleship"
- 1 navio de tamanho 3, o "Cruiser"
- 1 navio de tamanho 3, o "Submarine"
- 1 navio de tamanho 2, o "Destroyer"

Isso significa que voc� *precisa* definir a posi��o de todos esses navios no tabuleiro. O restante do tabuleiro ser� composto por �gua (automaticamente).

------

## Jogabilidade

No in�cio do jogo, os navios s�o posicionados conforme a estrat�gia definida (antes da interface gr�fica ser exibida). Em seguida, a tela do jogo apresenta dois tabuleiros: um para o jogador e outro para o oponente, com todas as posi��es inicialmente exibidas em duas formas: azul claro, para �gua; e azul escuro para mostrar onde os navios est�o posicionados.
Como o jogo � automatizado, n�o h� problemas em mostrar as posi��es dos navios durante a execu��o, mas isso n�o significa que, na implementa��o do c�digo, voc� saber� onde os navios do oponente foram inicializados.

A cada rodada, o jogador realiza um disparo em um quadrado do tabuleiro do oponente, e o resultado do tiro � exibido de acordo com os seguintes casos:

- **�gua:** o quadrado fica **cinza** com o emoji ?, pois o tiro foi em uma posi��o sem navio, isto �, posi��o de �gua;
- **acertou:** o quadrado fica **amarelo** com o emoji ?? se acertar uma posi��o de um navio.
- **afundou:** o quadrado fica **amarelo** com o emoji ?? se afundar um navio, isto �, se o tiro atingir a �ltima posi��o de um dos navios da frota.

### Exemplo de tabuleiro:
![Exemplo de tabuleiro](figures/exemplo_tabuleiro.png){ width=600px }

No imagem acima temos uma demonstra��o de um jogo em andamento. Perceba os ataques que deram certo (??), os que n�o acertaram (?), e os navios afundados (??), assim como as posi��es em azul mais escuro onde os navios foram posicionados.

### Bots
No modo *Aluno vs Bot*, o jogador implementado pelo aluno enfrentar� um bot com estrat�gia predefinida. Voc� pode consultar o c�digo do bot para entender sua l�gica de posicionamento e ataque, por�m, **est� proibido copiar estrat�gias do bot**. Voc� precisa criar a sua pr�pria estrat�gia.

Temos dois bots dispon�veis:

**1.** `bot_linear.py`: um bot que utiliza uma estrat�gia linear tanto para posicionar os navios quanto para atacar. Na fase de posicionamento, ele organiza os navios em linha reta (horizontal ou vertical) e de forma agrupada. Durante o ataque, ele dispara sequencialmente ao longo de uma linha;
**2.** `bot_random.py`: um bot que posiciona os navios aleatoriamente em linhas horizontais e ataca os navios aleatoriamente;

> **IMPORTANTE:**
> Sua implementa��o n�o deve buscar vencer um bot em especifico. Caso os avaliadores detectem que a sua implementa��o tenta reconhecer contra qual bot est� jogando, a nota do projeto ser� afetada.


------

## Estrutura do Projeto

A estrutura do projeto � composta por diversos arquivos, cada um com uma fun��o espec�fica. Abaixo, voc� encontrar� uma breve descri��o de cada um deles:

### Constantes
No arquivo `constants.py`, voc� encontrar� algumas constantes que podem ser �teis para a implementa��o do seu jogador. As constantes s�o:
- `TABULEIRO_TAMANHO`: tamanho do tabuleiro (10);
- `NAVIOS`: dicion�rio em que cada chave � o nome do navio e o valor � o tamanho do dele;

Neste mesmo arquivo, temos a [Enumera��o](https://docs.python.org/3/library/enum.html) chamada `StatusTab` com os poss�veis estados do tabuleiro, representados por inteiros. Esses estados s�o:
- `AGUA`: representa uma posi��o do tabuleiro que teve um ataque sem acerto;
- `NAVIO_ENCONTRADO`: representa uma posi��o de navio encontrado (acerto);
- `NAVIO_INTEIRO_ATINGIDO`: representa uma posi��o de navio afundado (afundado);
- `DESCONHECIDO`: representa uma posi��o que ainda n�o foi atingida para saber se tem navio ou n�o;
Para acessar estas constantes, garanta que o Enum esteja importado (`from constants import StatusTab`), e utilize `StatusTab.NOME_DA_CONSTANTE.value` para acessar o valor inteiro correspondente (ex: `StatusTab.AGUA.value`).



J� no arquivo `config.py`, voc� encontrar� somente duas constantes:
- `DELAY`: tempo de espera entre os ataques (em segundos). Quando estiver testando seu c�digo, voc� pode aumentar ou diminuir esse valor para facilitar a visualiza��o do jogo;
- `FINAL_DELAY`: tempo de espera para fechar a tela do jogo (em segundos).

------

### Classes

Seu projeto � composto por **cinco tipos de classes principais**, cada uma com um papel fundamental no jogo. Confira abaixo um resumo do que cada uma faz:


### `Navio` (arquivo `_ship.py`)

Representa um navio no tabuleiro.  
Essa classe **n�o tem m�todos**, apenas atributos:

- `nome`: string que representa o nome do navio (ex: "Carrier");
- `tamanho`: inteiro que indica o tamanho do navio;
- `coords`: lista de tuplas com as posi��es ocupadas pelo navio no tabuleiro (`list[tuple[int,int]]`);
- `posicoes_atingidas`: lista de tuplas com as posi��es que j� foram atingidas.
- *Aten��o*: O atributo `nome` � definido automaticamente ao posicionar o navio. Voc� n�o deve modificar esse valor diretamente, mas pode acess�-lo para verificar o nome do navio.

---

### `Ataque` (arquivo `_attack.py`)

Representa um ataque feito por um jogador.

- `x` e `y`: inteiros que indicam as coordenadas do ataque.  
O **construtor j� garante** que os valores estejam dentro dos limites do tabuleiro. Caso n�o estejam, o construtor ir� gerar um erro.

---

### `PosMatriz` (arquivo `_matrix.py`)
Representa uma posi��o no tabuleiro, com os seguintes atributos:
- `status`: inteiro que representa o status da posi��o de acordo com as contantes definidas no arquivo `constants.py`. Esse inteiro vem do Enum `StatusTab` (ex: `StatusTab.AGUA.value`);
- `nome_navio_atingido`: string do nome do tipo de navio que ocupa a posi��o, caso exista um navio ali. Se n�o houver navio, o valor ser� uma string vazia (`""`);
  - *Aten��o*: O valor do atributo `nome_navio_atingido` � **definido automaticamente** quando um navio � posicionado no tabuleiro. Voc� n�o deve modificar esse valor diretamente, mas pode acess�-lo para verificar se uma posi��o cont�m um navio ou n�o;

---

### `AlunoPlayer` (arquivo `player_aluno.py`)

**Ela representa o seu jogador**! Ou seja, � neste arquivo que voc� deve implementar a sua estrat�gia de ataque e posicionamento dos navios.
Essa classe possui os seguintes atributos:

- `movimentos_realizados`: lista de objetos `Ataque` (hist�rico dos ataques);
- `tabuleiro`: objeto da classe `Tabuleiro`, que representa o tabuleiro do jogador.
- `nome`: o nome da equipe jogador.

E possui os seguintes m�todos (que devem ser implementados):
- `jogar(self, estado_atual_oponente, navios_afundados) -> Ataque`: define a estrat�gia de ataque.  
  - `estado_atual_oponente`: estado do tabuleiro do oponente, representada por uma matriz 10x10 composta por objetos do tipo `PosMatriz`. Isso significa que voc� pode acessar (mas n�o modificar) o estado p�blico do tabuleiro do oponente para saber quais posi��es atingidas s�o parte de um navio ou n�o. 
    - Por exemplo, se voc� quiser saber se a posi��o (2, 3) do tabuleiro do oponente � um navio ou n�o, voc� pode verificar o status da posi��o acessando `estado_atual_oponente[2][3].status` e verificar se o valor � igual `StatusTab.NAVIO_ENCONTRADO.value` ou `StatusTab.NAVIO_INTEIRO_ATINGIDO.value`. Para saber se a posi��o (2, 3) cont�m um navio, voc� pode acessar o atributo `navio` da posi��o acessando `estado_atual_oponente[2][3].nome_navio_atingido` e verificar se o valor � diferente de `""`.;
  - `navios_afundados`: lista dos nomes dos navios j� afundados. Lembre-se de que na constante `NAVIOS` do arquivo `constants.py` o nome do navio � a chave e o tamanho � o valor. Isso pode te ajudar a identificar os tamanhos dos navios dessa lista.
  
- `posicoes_navios(self) -> list[Navio]`: define onde os navios ser�o posicionados no in�cio do jogo.


---

### Bots j� implementados

- `BotPlayerLinear` (arquivo `bot_linear.py`)
- `BotPlayerRandom` (arquivo `bot_random.py`)

Esses bots funcionam como exemplos, com estrat�gias simples de jogo.  
Voc� pode **analisar** como eles funcionam, mas **n�o deve copi�-los ou adapt�-los** diretamente.

---

### `Tabuleiro` (arquivo `_board.py`)

Representa o tabuleiro do jogador, com os seguintes m�todos (os quais n�o devem ser alterados):

- `receber_ataque(ataque)`: atualiza o tabuleiro com base no ataque recebido;
- `posicionar_navio(navio)`: posiciona um navio no tabuleiro;
- `estado_publico()`: retorna a vis�o p�blica do tabuleiro, sem mostrar navios ocultos ainda n�o atingidos;
- `navios_afundados()`: lista os navios j� afundados;
- `todos_afundados()`: diz se todos os navios foram destru�dos.

#### Atributos do Tabuleiro

- `matriz`: matriz 10x10 com os seguintes valores constitu�da de objetos do tipo `PosMatriz`. Essa matriz representa o estado do tabuleiro do jogador, isto �, cont�m as posi��es dos navios e os ataques realizados;
- `matriz_visivel`: matriz 10x10 com os seguintes valores constitu�da de objetos do tipo `PosMatriz`. Essa matriz representa o estado do tabuleiro a ser disponibilizado ao oponente, isto �, n�o mostra os navios ocultos ainda n�o atingidos;
- `navios`: lista de navios posicionados;
- `afundados`: lista de navios j� destru�dos.


------

### O que devo implementar?
Voc� deve modificar **apenas** o arquivo `player_aluno.py`. Nele, � obrigat�rio implementar os m�todos `posicoes_navios(self)` e `jogar(self, estado_atual_oponente, navios_afundados)`, descritos acima.

Al�m disso, **substitua** o trecho `self.nome = "{NOME_DA_EQUIPE}"` no construtor (`__init__`) pelo seu nome da sua equipe, para que ele seja exibido corretamente na interface do jogo.


Voc� pode consultar os outros arquivos para entender como o jogo funciona, mas n�o deve modific�-los, exceto a constante `DELAY` no arquivo `config.py`, que pode ser alterada para facilitar a visualiza��o da simula��o do jogo ao alterar a velocidade do jogo.

------

## Torneio

O torneio avaliar� a efici�ncia da estrat�gia desenvolvida e ser� usado para determinar a sua nota na atividade. Para isso, ser�o realizadas diversas partidas com cada um dos tipos de bot (linear e aleat�rio).

Ser�o calculadas as seguintes estat�sticas para avaliar a estrat�gia utilizada:
  - N�mero de jogos (500 ou mais)
  - N�mero de vit�rias do aluno
  - N�mero de derrotas do aluno
  - N�mero m�ximo de ataques do aluno
  - N�mero m�nimo de ataques do aluno
  - M�dia de n�mero de ataques do aluno
  - Mediana do n�mero de ataques do aluno
  - Desvio padr�o do n�mero de ataques do aluno

------
## Competi��o entre os players de alunos
Al�m do torneio contra os bots, haver� uma competi��o entre os alunos. Os alunos competir�o entre si, em um esquema de torneio, onde cada aluno jogar� contra todos os outros alunos. O aluno que vencer mais partidas ser� o campe�o.

Para participar, voc� deve preencher o seguinte formul�rio:
https://forms.gle/MTko33rK2jFZfNMi9

------

## Executando Simula��es

### Pr�-requisitos
1. **Instale o Pygame** (para rodar o jogo gr�fico):
   pip install pygame

2. **Instale o Tqdm** (para barra de progresso no torneio):
   pip install tqdm


### Modo *Aluno vs Bot*

Neste modo, o seu jogador enfrentar� um bot de acordo com o par�metro que voc� escolher. Voc� pode jogar com ou sem interface gr�fica (GUI). No caso de n�o querer a interface gr�fica, as jogadas ser�o exibidas no terminal.

Com GUI:
- bot linear: 
  python game.py -l

- bot aleat�rio: 
  python game.py -r

Sem GUI:
- bot linear:
  python game.py -l --no-gui

- bot aleat�rio:
  python game.py -r --no-gui


O resultado do jogo ser� exibido na tela, mostrando o n�mero de rodadas e o vencedor. Al�m disso, um arquivo chamado `resultados.txt` ser� gerado na mesma pasta do seu c�digo, contendo os resultados do jogo.

### Modo *Torneio*

Neste modo, ser�o executados v�rios testes da sua implementa��o contra os bots. O resultado ser� exibido em um arquivo CSV chamado `resultados_torneio.txt`, que ser� gerado na mesma pasta do seu c�digo.

Para executar o torneio, utilize o seguinte comando:
python tournament.py

## Entrega

Voc� deve entregar apenas o arquivo `player_aluno.py` no Google Classroom, no seguinte padr�o:

1. No in�cio do arquivo `player_aluno.py`, preencha o coment�rio com:
    - Nome Completo do Aluno que est� entregando
    - RA do Aluno que est� entregando
    - Nome Completo do outro membro da dupla
    - RA do outro membro da dupla
2. Na hora de entregar, renomeie o arquivo `player_aluno.py` para `player_<RA_DO_ALUNO1>_<RA_DO_ALUNO2>.py`, em que `<RA_DO_ALUNO1>` e `<RA_DO_ALUNO2>` s�o os RAs dos alunos da equipe. Por exemplo, se o RA do aluno 1 for `123456` e o RA do aluno 2 for `654321`, o arquivo deve ser renomeado para `player_123456_654321.py`. Note que o seu programa n�o vai funcionar com esse nome, ent�o se voc� for rodar o jogo, voc� deve renome�-lo de volta para `player_aluno.py`.
3. O outro membro da dupla deve enviar um coment�rio particular no Classroom dizendo que faz parte da dupla.

� obrigat�rio fazer a entrega em dupla.

## Nota
A sua nota ser� determinada pelo n�mero de vit�rias no torneio, sendo que o bot linear e o bot aleat�rio ser�o executados 1000 vezes cada um. A nota ser� calculada com a seguinte f�rmula:
**Nota = min(10, max(0, 10 * (Vit�rias - 900) / 900))**

Ou seja, a nota ser� calculada com base no n�mero de vit�rias do aluno, sendo que o aluno ter� nota 0 se tiver 900 vit�rias ou menos, e nota 10 se tiver 1800 vit�rias ou mais. Para valores entre 900 e 1800 vit�rias, a nota ser� calculada proporcionalmente.

### Exemplos:

- `900` vit�rias ? Nota = min(10, max(0, 10 * (900 - 900) / 900)) = 0
- `1350` vit�rias ? Nota = min(10, max(0, 10 * (1350 - 900) / 900)) = 5
- `1800` ou mais vit�rias ? Nota = min(10, max(0, 10 * (1800 - 900) / 900)) = 10
