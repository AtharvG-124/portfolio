import random

# ------------------------------Variables-------------------------------
board = ['-', 8, '-', 4, 3, '-', 9, '-', '-'
        , '-', 3, '-', '-', '-', '-', '-', '-', '-'
        , 2, '-', '-', '-', 7, 5, 6, '-', '-'
        , '-', '-', '-', 2, '-', '-', 5, 3, '-'
        , '-', '-', 4, '-', '-', '-', 7, '-', '-'
        , '-', 6, 3, '-', '-', 4, '-', '-', '-'
        , '-', '-', 6, 1, 8, '-', '-', '-', 5
        , '-', '-', '-', '-', '-', '-', '-', 8, '-'
        , '-', '-', 1, '-', 5, 9, '-', 7, '-']

border = ["=", "=", "=", "=", "=", "++", "=", "=", "=", "=", "=", "++", "=", "=", "=", "=", "="]
sec1 = [0, 1, 2, 8, 9, 10, 17, 18, 19]
sec2 = [4, 5, 6, 12, 13, 14, 21, 22, 23]
sec3 = [7, 8, 9, 15, 16, 17, 24, 25, 26]

sec4 = [27, 28, 29, 36, 37, 38, 45, 46, 47]
sec5 = [30, 31, 32, 39, 40, 41, 48, 49, 50]
sec6 = [33, 34, 35, 42, 43, 44, 51, 52, 53]

sec7 = [54, 55, 56, 63, 64, 65, 72, 73, 74]
sec8 = [57, 58, 59, 66, 67, 68, 75, 76, 77]
sec9 = [60, 61, 62, 69, 70, 71, 78, 79, 80]

sections = [sec1, sec2, sec3, sec4, sec5, sec6, sec7, sec8, sec9]

# ------------------------------Functions-------------------------------
# converts a list to a string
def list_to_string(s):
    str1 = ' '
    return str1.join(s)


# Displays board
def display_board():
    # Section 1
    print(board[0], ' ', board[1], ' ', board[2], "||", board[3], ' ', board[4], ' ', board[5], "||", board[6], ' ',
          board[7], ' ', board[8])
    print(board[9], ' ', board[10], ' ', board[11], "||", board[12], ' ', board[13], ' ', board[14], "||", board[15],
          ' ', board[16], ' ', board[17])
    print(board[18], ' ', board[19], ' ', board[20], "||", board[21], ' ', board[22], ' ', board[23], "||", board[24],
          ' ', board[25], ' ', board[26])
    print(list_to_string(border))

    # Section 2
    print(board[27], ' ', board[28], ' ', board[29], "||", board[30], ' ', board[31], ' ', board[32], "||", board[33],
          ' ', board[34], ' ', board[35])
    print(board[36], ' ', board[37], ' ', board[38], "||", board[39], ' ', board[40], ' ', board[41], "||", board[42],
          ' ', board[43], ' ', board[44])
    print(board[45], ' ', board[46], ' ', board[47], "||", board[48], ' ', board[49], ' ', board[50], "||", board[51],
          ' ', board[52], ' ', board[53])
    print(list_to_string(border))

    # Section 3
    print(board[54], ' ', board[55], ' ', board[56], "||", board[57], ' ', board[58], ' ', board[59], "||",
          board[60], ' ', board[61], ' ', board[62])
    print(board[63], ' ', board[64], ' ', board[65], "||", board[66], ' ', board[67], ' ', board[68], "||",
          board[69], ' ', board[70], ' ', board[71])
    print(board[72], ' ', board[73], ' ', board[74], "||", board[75], ' ', board[76], ' ', board[77], "||",
          board[78], ' ', board[79], ' ', board[80])


# replaces a blank spot with the desired number
def choose_position():
    position = int(input("choose a position between 1 - 81: "))
    position = int(position) -1
    number = int(input("choose a number between 1-9: "))
    while number > 9:
        print("this number is not valid. Try again")
        number = int(input("choose a number between 1-9: "))

    if board[position] == "-":
        result = [position, number]
        return result
    else:
        print("you cant go there")
        choose_position()


def check_rows():

    r1 = []; r2 = []; r3 = []; r4 = []; r5 = []; r6 = []; r7 = []; r8 = []; r9 = []

    row_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    row_2 = [9, 10, 11, 12, 13, 14, 15, 16, 17]
    row_3 = [18, 19, 20, 21, 22, 23, 24, 25, 26]

    row_4 = [27, 28, 29, 30, 31, 32, 33, 34, 35]
    row_5 = [36, 37, 38, 39, 40, 41, 42, 43, 44]
    row_6 = [45, 46, 47, 48, 49, 50, 51, 52, 53]

    row_7 = [54, 55, 56, 57, 57, 58, 59, 60, 61]
    row_8 = [63, 64, 65, 66, 67, 68, 69, 70, 71]
    row_9 = [72, 73, 74, 75, 76, 77, 78, 79, 80]

    rows = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

    for i in range(9):
        r1.append(row_1[i]); r2.append(row_2[i]); r3.append(row_3[i]); r4.append(row_4[i]); r5.append(row_5[i])
        r6.append(row_6[i]); r7.append(row_7[i]); r8.append(row_8[i]); r9.append(row_9[i])
    x = 0
    x = x + 1
    if r1.count(x) > 1 or r2.count(x) > 1 or r3.count(x) > 1 or r4.count(x) > 1 or r5.count(x) > 1 \
        or r6.count(x) > 1 or r7.count(x) > 1 or r8.count(x) > 1 or r9.count(x) > 1:
        print("You can't put this number in this row")






    return

def check_columns():
    return





# ------------------------------Main Program-------------------------------

print("If you want to exit, press 0")
print('press any button to start ')
pos = input()
while pos != 0:
    display_board()
    choose_position()




