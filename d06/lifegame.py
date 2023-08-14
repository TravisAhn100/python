import tkinter as tk
import time
from random import *


board  = [[0] * 40 for _ in range(40)]
board2 = [[0] * 40 for _ in range(40)]

is_playing = False



def on_click(event):
    min_dim = min(canvas.winfo_reqwidth(), canvas.winfo_reqheight())
    cellw = min_dim / len(board)

    y = int(event.y // cellw)
    x = int(event.x // cellw)

    board[y][x] = 1 - board[y][x]
    print ("clicked at", event.x, event.y, y, x)
    print("asdsad")


def draw_board(canvas, board):
    min_dim = min(canvas.winfo_reqwidth(), canvas.winfo_reqheight())
    cellw = min_dim / len(board)

    for (y, row) in enumerate(board):
        for (x, cell) in enumerate(row):
            fill = 'white' if cell == 0 else 'black'
            canvas.create_rectangle(x * cellw, y * cellw, (x + 1) * cellw, (y + 1) * cellw, fill = fill, outline="")

window = tk.Tk()
window.title("I am Jesus.")
window.resizable(True, True)
canvas = tk.Canvas(window, width=1000, height=800, background='gray')
canvas.bind('On Click', on_click)
canvas.pack()
def callback(event):
    print ("clicked at", event.x, event.y)


def on_button(event):
    print("HEllo")
    global is_playing 
    is_playing = not is_playing
    turn_on.config(text=("stop [=]" if is_playing else "play [>]"))
    turn_on.update()

turn_on = tk.Button(window, text="play [>]", width=100, height=100)
turn_on.bind("<Button-1>", on_button)
canvas.bind("<Button-1>", on_click)

turn_on.pack()

def lifegame_step(board_prev):
    for (y_num,y_list) in enumerate(board):
        for (x_num,x_row) in enumerate(y_list):
            # print(end='')
            if x_row == 1:
                [y,x] = x_surrounding_coord(board,y_num,x_num)
                count_coord(board,y_num,x_num)
                
def count_coord(board,y,x): 
    mt_list = []
    neighs  = x_surrounding_coord(board,y,x)
    for c in neighs:
        if board[c[0]][c[1]] == board[y][x]:
            mt_list += [c]
    return mt_list
            
            


def is_in_board(board, y, x):
    height = len(board)
    width  = len(board[0])
    return (0 <= x) and (x < width) \
       and (0 <= y) and (y < height)

def x_surrounding_coord(board, y, x):
    
    x_surrounding_list = [[1,1],[1,-1],[1,0],[0,1]]
    mt_list = []
    org_coord = [x,y]

    for coord_diff in x_surrounding_list:
        add_list_x = coord_diff[0] + org_coord[0]
        add_list_y = coord_diff[1] + org_coord[1]
        if (is_in_board(board, add_list_y, add_list_x)):
            add_list = [add_list_y, add_list_x]
            mt_list += [add_list]

        sub_list_x = org_coord[0] - coord_diff[0]
        sub_list_y = org_coord[1] - coord_diff[1] 
        if (is_in_board(board, sub_list_y, sub_list_x)):
            sub_list = [sub_list_y, sub_list_x]
            mt_list += [sub_list]
    
    return mt_list

print(x_surrounding_coord(board, 10, 10 ))
while True:
    draw_board(canvas, board)
    if (is_playing):
        lifegame_step(board)
    window.update()
