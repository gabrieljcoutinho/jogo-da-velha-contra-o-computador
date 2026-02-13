# Jogo da Velha (Tic-Tac-Toe) em Python

Este é um clássico Jogo da Velha desenvolvido em Python para ser jogado diretamente no terminal. O projeto coloca o usuário para enfrentar a inteligência da máquina em uma disputa de estratégia simples e divertida.

## Funcionalidades e Mecânicas

* **Modo Jogador vs IA:** O usuário joga como "X" e o computador assume o símbolo "O".
* **Tabuleiro Interativo:** Representação visual do tabuleiro 3x3 atualizada a cada turno no console.
* **IA Aleatória:** O computador processa os espaços vazios e realiza movimentos automáticos utilizando a biblioteca `random`.
* **Validação de Jogadas:** O sistema impede que o jogador escolha uma posição que já tenha sido ocupada.
* **Detecção Automática de Resultado:**
    * **Vitória/Derrota:** O jogo identifica padrões horizontais, verticais e diagonais.
    * **Empate:** Caso as 9 posições sejam preenchidas sem um vencedor, o jogo declara empate.

## Tecnologias Utilizadas

* **Python 3.x:** Linguagem de programação principal.
* **Biblioteca `random`:** Responsável por gerar as jogadas do oponente de forma imprevisível.

## Como Executar o Jogo

1.  Certifique-se de ter o Python instalado.
2.  Salve o código em um arquivo chamado `jogo_da_velha.py`.
3.  Execute o comando no terminal:
    ```bash
    python jogo_da_velha.py
    ```
4.  As posições são mapeadas de **0 a 8**, começando do topo esquerdo até a base direita:
    ```text
    0|1|2
    -+-+-
    3|4|5
    -+-+-
    6|7|8
    ```

## Estrutura do Código

* **`mostrar_tabuleiro()`:** Renderiza o estado atual da partida.
* **`checar_vitoria(simbolo)`:** Contém a lógica matemática das tuplas de vitória para validar se o jogador ou o computador ganhou.
* **`movimento_computador()`:** Filtra as posições disponíveis e sorteia uma jogada válida para a máquina.
* **Loop Principal:** Controla o sistema de turnos alternados entre "X" e "O".

---

*Desenvolvido como um exercício de lógica de programação, manipulação de listas e funções em Python.*
