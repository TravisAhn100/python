# importing image object from PIL
import math
from PIL import Image, ImageDraw

def draw_quad_arc(imgdraw, cx, cy, r, theta, S = 1):
        bbox = [(cx - S * r, cy - S * r), \
                (cx + S * r, cy + S * r)]
        print(bbox)
        imgdraw.arc(bbox, theta * 90, (theta + 1) * 90, width = 2)

quads = ((0, 0), (-1, 0), (-1, -1), (0, -1))
def draw_quadrangle(imgdraw, cx, cy, r, quad_mode, S = 1):
        lx = cx + quads[quad_mode][0] * r * S
        ly = cy + quads[quad_mode][1] * r * S
        quad = [(lx, ly), (lx + S * r, ly + S * r)]
        imgdraw.rectangle(quad, width = 1)

def move_center(x, y, r, theta, S = 1):
        if (theta % 2 == 0):
                return (x, y + S * r * (theta - 1))
        else:
                return (x - S * r * (theta - 2), y)

def draw_golden_spiral(fibonacci_list, w, h):
        img  = Image.new("RGB", (w, h))
        imgd = ImageDraw.Draw(img)

        last = 0
        x = (w // 2)
        y = (h // 2)
        theta = 0

        S = h / max(fibonacci_list) / 2

        for cur in fibonacci_list:
                draw_quadrangle(imgd, x, y, cur, theta, S)
                draw_quad_arc  (imgd, x, y, cur, theta, S)

                (x, y) = move_center(x, y, last, theta, S)
                theta = (theta + 1) % 4
                last = cur
                print(x,y)

        img.show()


