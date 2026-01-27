board = [" "] * 9

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

player = "X"

for turn in range(9):
    print_board()
    move = int(input(f"Player {player}, choose position (1-9): ")) - 1

    if board[move] == " ":
        board[move] = player
        player = "O" if player == "X" else "X"
    else:
        print("Invalid move!")
