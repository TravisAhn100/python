import tkinter as tk
import time
from random import *


board = [[0] * 40 for _ in range(40)]

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

# canvas= Canvas(root, width=100, height=100)
# canvas.bind("<Key>", key)
canvas.bind("<Button-1>", on_click)
# canvas.pack()
def on_button(event):
    print("HEllo")
    global is_playing 
    is_playing = not is_playing
    turn_on.config(text=("stop [=]" if is_playing else "play [>]"))
    turn_on.update()

turn_on = tk.Button(window, text="play [>]", width=100, height=100)
turn_on.bind("<Button-1>", on_button)
turn_on.pack()
# canvas.grid(ro?ow=1, column=0)

def lifegame_step(board):
    board[randrange(0, 40)][randrange(0, 40)] = 1
    board[randrange(0, 40)][randrange(0, 40)] = 0

while True:
    draw_board(canvas, board)
    if (is_playing):
        lifegame_step(board)
    window.update()
