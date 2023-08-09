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
            if y%2==1:
                if x%2==0:
                    line += BLACK_BG
                if x%2==1:
                    line += WHITE_BG
            if y%2==0:
                if x%2==0:
                    line += WHITE_BG
                if x%2==1:
                    line += BLACK_BG
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
board[0][-3]=bishop
board[0][2]=bishop
board[0][0]=rook
board[0][7]=rook

draw_board(board)
# for line in board:
#     print(line)
while True:
    selection = list(input())
    x = int(ord(selection[0].lower())) - 97
    y = int(selection[1])-1

    print(f"row: {x+1}, rank: {y+1}")
    if y>=8:
        print('invalid move')
        continue
    if board[y][x]=='.':
        print('blank')
    if board[y][x]=='♘':
        print('knight %s selected'%selection)
        movement = list(input())
        x2 = ord(movement[0].lower()) - 97
        y2 = int(movement[1])-1
        board[y][x]='.'
        board[y2][x2]='♘'
        draw_board(board)
    if board[y][x]=='♖':
        print('rook %s selected' % str(selection))
        movement = list(input())
        x2 = ord(movement[0].lower()) - 97
        y2 = int(movement[1])-1
        print(f"row2: {x2+1}, rank2: {y2+1}")
        board[y][x]='.'
        board[y2][x2]='♖'
        draw_board(board)
        
