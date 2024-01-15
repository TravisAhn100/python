import pygame, sys
from pygame.locals import *
pygame.init()
screen= pygame.display.set_mode((1000,600))
surface = pygame.display.set_mode((400,300))
color = (255,0,0)
r1 = pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
