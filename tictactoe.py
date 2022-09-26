def main():
    player = next_player("")
    board = create()
    while not (winner(board) or draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!")
    play_again()

    
def play_again():
    again = input(f"Want to play again? y/n: ")
    if again == "y":
        return main()


def create():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board


def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}\n-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}\n-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()


def draw(board):
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
    return True


def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])


def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player


def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"


if __name__ == "__main__":
    main()
