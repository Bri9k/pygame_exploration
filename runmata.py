from automata import *
import rules
import random
import pygame
import sys

height = int(sys.argv[1])
breadth = int(sys.argv[2])

bitmap = [[False] * breadth for i in range(height)]
bitmap[height // 2][breadth // 2] = True

dale = cellularAutomaton(bitmap, rules.mann)

side = 10
pygame.init()
screensize = [dale.length * side, dale.breadth * side]
screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()

going = True
while going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False

    dale.propagate()

    screen.fill((0, 0, 0))
    for i in range(height):
        for j in range(breadth):
            if(dale.cell(i, j)):
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i * side, j * side, side - 1, side - 1), 0)

    pygame.display.flip()
    clock.tick(7)
