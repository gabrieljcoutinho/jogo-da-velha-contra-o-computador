import random

# Criar tabuleiro vazio
tabuleiro = [" " for _ in range(9)]

# Função para mostrar tabuleiro
def mostrar_tabuleiro():
    print(f"{tabuleiro[0]}|{tabuleiro[1]}|{tabuleiro[2]}")
    print("-+-+-")
    print(f"{tabuleiro[3]}|{tabuleiro[4]}|{tabuleiro[5]}")
    print("-+-+-")
    print(f"{tabuleiro[6]}|{tabuleiro[7]}|{tabuleiro[8]}")

# Função para checar vitória
def checar_vitoria(simbolo):
    vitorias = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(tabuleiro[a]==tabuleiro[b]==tabuleiro[c]==simbolo for a,b,c in vitorias)

# Função para movimentos válidos do computador
def movimento_computador():
    possiveis = [i for i, valor in enumerate(tabuleiro) if valor == " "]
    return random.choice(possiveis)

# Loop principal
for i in range(9):
    mostrar_tabuleiro()

    # Turno do jogador
    if i % 2 == 0:
        while True:
            pos = int(input("Escolha sua posição (0-8): "))
            if tabuleiro[pos] == " ":
                tabuleiro[pos] = "X"
                break
            else:
                print("Essa posição já está ocupada! Escolha outra.")
        if checar_vitoria("X"):
            mostrar_tabuleiro()
            print("Parabéns! Você venceu!")
            break
    # Turno do computador
    else:
        pos = movimento_computador()
        tabuleiro[pos] = "O"
        print(f"Computador jogou na posição {pos}")
        if checar_vitoria("O"):
            mostrar_tabuleiro()
            print("O computador venceu!")
            break
else:
    mostrar_tabuleiro()
    print("Empate!")
