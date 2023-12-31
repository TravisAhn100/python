from random import random

BLACK_BG = "\033[40;97m"
WHITE_BG = "\033[107;30m"
BRED_BG  = "\033[101m"
RESET    = "\033[m"

selected = [-1, -1] ## None

"""
purpose: validates the movement for the knight
input  : from & to coordinates
returns: (True/False) wheter the move is legal for the knight
"""
def knight_movement(board, y, x, y2, x2):
    mal_movement=[[y+1,x+2],[y+1,x-2],[y-1,x+2],[y-1,x-2],[y+2,x+1],[y+2,x-1],[y-2,x+1],[y-2,x+1]]
    for c in mal_movement:
        if [y2,x2] == c:
            return True
    return False

"""""
purpose: validates the movement for the rook
input  : from & to coordinates
returns: whether the move is legal for the rook
"""""
def rook_movement(y, x, y2, x2):
    if x==x2 and y==y2:
        return False
    if x==x2 or y==y2:
        return True
    return False

"""
purpose: selects an (y,x) coord from user input.
         if couldn't, repeats until it can
input  : chess board
returns: a *valid* pair of coord (y, x)
"""
def select_coord(board): 
    while True:
        selection = list(input())
        x = int(ord(selection[0].lower())) - 97
        y = int(selection[1])-1
        if y>=8 or x>=8 or y<0 or x<0:
            print('invalid move')
            continue
        else:
            break
    global selected
    selected = [y, x]
    return [y, x]

"""
purpose: prints the coord of the piece
input  : coordination of the selected piece
effect : prints message to standard output
"""
def coord_message(y, x, p):
    if p=='♘':
         print('%s %s selected.'% ('knight',[x+1,y+1]))
    if p=='♖':
        print('%s %s selected.'% ('rook',[x+1,y+1]))
    print(f"row: {x+1}, rank: {y+1}")


    

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
            if selected == [y, x]:
                line += BRED_BG
 
            line += cell
            
            if x == 7:
                line += ' '
            
        line += RESET
        print(line)


l=['.' for i in range(8)]
board= [['.' for i in range(8)]for j in range(8)]
# print(board)

knight = '♘'
rook = '♖'
board[0][ 1]=knight
board[0][-2]=knight
# board[0][-3]=bishop
# board[0][2]=bishop
board[0][0]=rook
board[0][7]=rook

draw_board(board)

while True:
    [y, x] = select_coord(board)

    draw_board(board)
    coord_message(x,y,board[y][x])

    if board[y][x]=='.':
        print('blank')
        continue

    [y2, x2] = select_coord(board)

    if board[y][x] == '♘':    
        knight_movement(board, y, x , y2 , x2)
        if knight_movement(board, y, x , y2 , x2) == False:
            print('invalid movement') 
            continue
        board[y][x]='.'
        board[y2][x2]='♘'
        draw_board(board)

    if board[y][x] == '♖':
        rook_movement(x,y,x2,y2)
        if rook_movement( y, x , y2 , x2) == False:
            print('invalid movement') 
            continue
        board[y][x]='.'
        board[y2][x2]='♖'
        draw_board(board)
        
