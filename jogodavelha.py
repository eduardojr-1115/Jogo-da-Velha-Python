"""
Jogo da Velha (Tic-Tac-Toe) CLI
Desenvolvido por: Eduardo Santos
Objetivo: Exercitar lógica de matrizes, funções e tratamento de erros.
"""

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

jogador = "X"

def exibe_tabuleiro():
    """Exibe o estado atual do tabuleiro no terminal."""
    print("\n")
    for i, linha in enumerate(tabuleiro):
        print(" " + " | ".join(linha))
        if i < 2:
            print("---" * 4)
    print("\n")

def fazer_jogada(linha, coluna, jogador_atual):
    """Valida e executa a jogada no tabuleiro."""
    if not (0 <= linha <= 2 and 0 <= coluna <= 2):
        print("Erro: Digite números entre 0 e 2!")
        return False
    
    if tabuleiro[linha][coluna] != " ":
        print("Erro: Esta posição já está ocupada!")
        return False
    
    tabuleiro[linha][coluna] = jogador_atual
    return True

def verificar_vitoria():
    """Verifica todas as condições de vitória (linhas, colunas e diagonais)."""
    
    # Verificar linhas
    for linha in range(3):
        if tabuleiro[linha][0] != " " and tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2]:
            return True
            
    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] != " " and tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna]:
            return True
            
    # Verificar diagonais (Correção aplicada aqui)
    if tabuleiro[1][1] != " ":
        # Diagonal principal
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
            return True
        # Diagonal secundária
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
            return True
    
    return False

def verificar_empate():
    """Verifica se não há mais espaços vazios (velha)."""
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

def iniciar_jogo():
    """Função principal que gerencia o fluxo do jogo."""
    global jogador
    print("--- BEM-VINDO AO JOGO DA VELHA ---")
    exibe_tabuleiro()

    while True:
        print(f"Vez do jogador: {jogador}")
        
        try:
            l = int(input("Digite a linha (0, 1, 2): "))
            c = int(input("Digite a coluna (0, 1, 2): "))
            
            if fazer_jogada(l, c, jogador):
                exibe_tabuleiro()
                
                if verificar_vitoria():
                    print(f"PARABÉNS! O jogador '{jogador}' venceu!")
                    break
                
                if verificar_empate():
                    print("O jogo empatou (Deu velha)!")
                    break
                
                # Alterna o jogador
                jogador = "O" if jogador == "X" else "X"
            else:
                continue # Pede a jogada novamente se houver erro de validação
                
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números inteiros.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    iniciar_jogo()