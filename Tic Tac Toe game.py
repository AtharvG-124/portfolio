# ------------------Variables--------------------
board = ["-", "-", "-"
    , "-", "-", "-"
    , "-", "-", "-"]

# if game is going
game_going = True

# Winner?
winner = None

# Whose turn is it?
current_player = "X"


# -------------------Functions--------------------
def display_board():
    print("\n")
    print(board[0], " | ", board[1], " | ", board[2] + "     1 | 2 | 3")
    print(board[3], " | ", board[4], " | ", board[5] + "     4 | 5 | 6")
    print(board[6], " | ", board[7], " | ", board[8] + "     7 | 8 | 9")
    print("\n")

def play_game():
    display_board()
    handle_turn(current_player)
    while game_going:
        change_player()
        handle_turn(current_player)
        check_end_game()


    # Game has ended
    if winner == "X" or winner == "O":
        print(winner, " won!")
    elif winner == None:
        print("Tie.")

def handle_turn(player):
    print(player + "'s turn")
    position = input("Choose a position between 1-9: ")

    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position between 1-9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again")

    board[position] = player
    display_board()

def check_end_game():
    check_if_win()
    check_if_tie()

def check_if_win():

    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        # no win
        winner = None
    return

def check_rows():
    global game_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2:
        game_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

def check_if_tie():
    global game_going

    if "-" not in board:
        game_going = False
    return

def change_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


# -------------------------Main Program------------------------

play_game()

'''
board
display board
play game
handle turn
check win
    check rows
    check columns
    check diagonals
-check tie
flip player
'''
