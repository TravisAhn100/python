from random import random

BLACK_BG = "\033[40;97m"
WHITE_BG = "\033[107;30m"
RESET    = "\033[m"

def draw_board(board): 
    line = " "
    for x in range(8):
        line += ' ' + chr(ord('A') + x) 
    print(line)

    for (y, row) in enumerate(board):
        line = chr(ord('1') + y)
        for (x, cell) in enumerate(row):
            line += ' '
            if (random() < 0.5):
                line += BLACK_BG
            else:
                line += WHITE_BG
            line += cell
        line += RESET
        print(line)

# white knight= n , black knight= N
l=['.' for i in range(8)]
board= [['.' for i in range(8)]for j in range(8)]
# print(board)

knight='♘'

board[0][ 1]=knight 
board[0][-2]=knight

draw_board(board)
# for line in board:
#     print(line)

selection = list(input())
row = ord(selection[0].lower()) - 97
rank = int(selection[1])-1

print(f"row: {row}, rank: {rank}")

if board[rank][row]=='.':
    print('.')
if board[rank][row]=='♘':
    print('selected')
    movement = list(input())
    row2 = ord(movement[0].lower()) - 97
    rank2 = int(movement[1])-1


    print(f"row2: {row2}, rank2: {rank2}")

    board[rank][row]='.'
    board[rank2][row2]='♘'
    for line in board:
        print(line)
    