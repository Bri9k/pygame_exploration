from automata import *
import random
import pygame
import sys

def mann(bitmap, length, breadth, i, j):
    if i == length - 1 or j == breadth - 1 or i == 0 or j == 0:
        return False

    count = 0
    for a in range(i - 1, i + 2):
        for b in range(j - 1, j + 2):
            if (not (i == a and b == j)) and bitmap[a][b]:
                count += 1

    # loneliness or overcrowding
    if count % 3 == 1:
        return True
    elif i == length // 2 and j == breadth // 2:
        return True
    else:
        return False
 
def conway(bitmap, length, breadth, i, j):
    # kill the edge case headaches
    if i == length - 1 or j == breadth - 1 or i == 0 or j == 0:
        return bitmap[i][j]

    count = 0
    for a in range(i - 1, i + 2):
        for b in range(j - 1, j + 2):
            if (not (i == a and b == j)) and bitmap[a][b]:
                count += 1

    # loneliness or overcrowding
    if count <= 2 or count >= 5:
        return False
    else:
        return True

height = int(sys.argv[1])
breadth = int(sys.argv[2])

bitmap = [[True] * breadth for i in range(height)]

dale = cellularAutomaton(bitmap, mann)

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
