# 🤖 Bot Estratégico para Batalha Naval (MC102)

> Um agente autônomo em Python que utiliza uma estratégia de ataque em dois estágios para jogar Batalha Naval de forma eficiente e lógica, alcançando 100% de vitórias em testes contra bots de referência.

Este projeto foi desenvolvido para a disciplina de MC102 e consiste na criação de um bot com uma inteligência artificial que toma decisões informadas para maximizar as chances de vitória no jogo Batalha Naval.

---

### 🎬 Demonstração em Ação

Abaixo, uma demonstração do bot em uma partida completa, desde o primeiro tiro até a vitória.

![Demonstração do Bot em Ação](https://github.com/user/repo/assets/...)

---

### ✨ Principais Funcionalidades

* **Estratégia de Ataque Híbrida:** O bot alterna inteligentemente entre um modo de **"Busca"** e um modo de **"Destruição"** para otimizar cada jogada.
* **Busca Otimizada com Padrão Xadrez:** Em vez de ataques aleatórios, o bot varre o tabuleiro em um padrão intercalado (`(linha + coluna) % 2 == 0`), cobrindo o campo de forma mais inteligente e reduzindo drasticamente os tiros necessários para o primeiro acerto.
* **Lógica de Destruição Direcionada:** Ao encontrar um navio, o bot foca nos arredores do acerto para determinar a orientação (vertical/horizontal) e afundá-lo rapidamente em uma sequência linear de ataques.
* **Posicionamento Estratégico:** A frota é posicionada nos cantos do tabuleiro, uma tática para maximizar o "espaço vazio" no centro e dificultar a fase de busca do oponente.

---

### 🏆 Resultados do Torneio

Para validar a eficiência da estratégia, o bot foi submetido a um torneio com 2.000 partidas simuladas (1.000 contra cada bot de referência). Os resultados demonstram a robustez do algoritmo:

```
-----Resultados contra Bot-Linear:
- Número de jogos: 1000
- [cite_start]Número de vitórias do aluno: 1000 [cite: 1]
- [cite_start]Número de derrotas do aluno: 0 [cite: 1]
- [cite_start]Média de número de ataques do aluno: 47.80 [cite: 1]

-----Resultados contra Bot-Random:
- Número de jogos: 1000
- [cite_start]Número de vitórias do aluno: 1000 [cite: 2]
- [cite_start]Número de derrotas do aluno: 0 [cite: 2]
- [cite_start]Média de número de ataques do aluno: 52.69 [cite: 2]

ANÁLISE GERAL DE TODOS OS JOGOS:
- Número total de jogos: 2000
- Número total de vitórias do aluno: 2000
- Número total de derrotas do aluno: 0
- Média de número de ataques do aluno em todos os jogos: 50.24
```

---

### 🛠️ Tecnologias e Dependências

* **Python:** Linguagem principal para a implementação da lógica.
* **Pygame:** Utilizado para a construção da interface gráfica do jogo.
* **Tqdm:** Para a visualização da barra de progresso durante os torneios.
* **Conceitos Aplicados:** Lógica de Algoritmos, Máquinas de Estado Finito, Estruturas de Dados (Matrizes).

---

### 🚀 Executando o Projeto

#### Pré-requisitos

Garanta que você tenha o Pygame e o Tqdm instalados:
```bash
pip install pygame tqdm
```

#### Rodando uma Partida (Aluno vs. Bot)

Você pode executar uma única partida contra os bots com ou sem interface gráfica.

* **Contra o Bot Linear (com GUI):**
    ```bash
    python game.py -l
    ```

* **Contra o Bot Aleatório (com GUI):**
    ```bash
    python game.py -r
    ```

* Para rodar **sem a interface gráfica**, adicione a flag `--no-gui` a qualquer um dos comandos acima.

#### Rodando o Torneio Completo

Para executar a simulação de 2.000 jogos e gerar o arquivo `resultado_torneio.txt`, utilize o comando:
```bash
python tournament.py
```

---

### 👨‍💻 Autores

* **Cristiano Gomes de Paula Filho**
* **Daniel Vessalli**
