#
# Tic Tac Toe Game inspired by a video I've come across on the Internet.
# 2 player initial version.
# 

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
player1 = "X"
player2 = "O"

for round in range(9):
    if round % 2 == 0:
        print(f"X's turn")
        move = input("Play in a space (1-9): ")
        for i in range(3):
            for j in range(3):
                if board[i][j] == move:
                    board[i][j] = player1
        if win(board):
            print("\n\nX wins!")
            break
    else:
        print(f"O's turn")
        move = input("Play in a space (1-9): ")
        for i in range(3):
            for j in range(3):
                if board[i][j] == move:
                    board[i][j] = player2
        if win(board):
            print("\n\nO wins!")
            break
    show_board(board)
print("\n")
show_board(board)