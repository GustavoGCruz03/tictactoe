#
# Tic Tac Toe Game inspired by a video I've come across on the Internet.
# 1 player vs Randomized AI
# 


import random

def show_board(b):
    for l in b:
        print(" | ".join(l))
""""
def not_a_play(b):
    for i in range(3):
        for j in range(3):
            if b[i][j] == "O" or b[i][j] == "X":
                print("This space is already taken. Take a look at the board and choose another!")
                return False
    return True
"""
def win(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] or b[0][i] == b[1][i] == b[2][i] or b[0][0] == b[1][1] == b[2][2] or b[0][2] == b[1][1] == b[2][0]:
            return True
    return False


board = [["1","2","3"],["4","5","6"],["7","8","9"]]
show_board(board)
print("Choose your simbol: X or O")
player1 = input("Player 1: ").upper()
player2 = "O" if player1 == "X" else "X"
## Player 2 is now randomized AI


for round in range(9):
    if round % 2 == 0:
        print(f"X's turn")
        if player2 == 'X':
            move = random.choice([str(i) for i in range(1, 10) if str(i) in [item for sublist in board for item in sublist]])
            print(f"AI plays in space {move}")
        else: move = input("Play in a space (1-9): ")
        for i in range(3):
            for j in range(3):
                if board[i][j] == move:
                    board[i][j] = 'X'
        show_board(board)
        if win(board):
            print("\n\nX wins!")
            break
    else:
        print(f"O's turn")
        if player2 == 'O':
            move = random.choice([str(i) for i in range(1, 10) if str(i) in [item for sublist in board for item in sublist]])
            print(f"AI plays in space {move}")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == move:
                        board[i][j] = player2
        else: move = input("Play in a space (1-9): ")
        for i in range(3):
            for j in range(3):
                if board[i][j] == move:
                    board[i][j] = 'O'
        show_board(board)
        if win(board):
            print("\n\nO wins!")
            break
        print("\n")

if not win(board): print("\n\nDraw:")
show_board(board)