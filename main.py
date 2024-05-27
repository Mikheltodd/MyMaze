import random
import time
import os 
import csv

def generate_board(size, options):
    board = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(random.choice(options))
        board.append(row)
    return board

def show_board(board):
    for row in board:
        print(" ".join(row))
    print()

def hide_value(board):
    row = random.randint(0, len(board) - 1)
    col = random.randint(0, len(board) - 1)
    hidden_value = board[row][col]
    board[row][col] = " "
    return hidden_value, board

def record_player(player, points):
    pass

def verify_answer(hidden_value, guess):
    if guess == hidden_value:
        print("¡Correcto!")
        correct_answer = True
    else:
        print(f"Incorrecto. El valor oculto era: {hidden_value}")
        correct_answer = False
    return correct_answer


def play_memory_game(options):
    size = int(input("Ingresa el tamaño del tablero (n x n): "))
    lives = 3
    points = 0
    round = 1
    while lives > 0:
        os.system('cls')
        board = generate_board(size, options)
        print(f"Ronda: #{round}")
        print(f"Vidas: x{lives}")
        print(f"Puntos: {points}")
        time.sleep(2)
        print("¡Memoriza el tablero!\n")
        show_board(board)
        time.sleep(size * 3)
        os.system('cls')
        print("¡Tiempo terminado! Ahora intenta recordar el valor oculto.\n")
        hidden_value, board = hide_value(board)
        show_board(board)
        guess = input("Ingresa el valor oculto: ")
        answer = verify_answer(hidden_value, guess)
        if not answer:
            lives -= 1
        else:
            print("Muy bien. Vamos a la siguiente ronda.")
            points += round * 5
            round += 1
        time.sleep(2)
    print(f"Tu puntaje es de {points} puntos")

def main():
    os.system('cls')
    print("Bienvenido al juego de adivinar.")
    options = ['A', 'B', 'C', 'D', 'E', '1', '2', '3', '4', '5', '@', '#', '$', '&']
    play_memory_game(options)
    while True:
        play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if play_again != 's':
            break
        play_memory_game(options)

if __name__ == "__main__":
    main()








