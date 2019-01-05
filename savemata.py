from automata import *
import pygame
import sys

arguements = len(sys.argv)
print(sys.argv)
if arguements == 1:
    height = 35
    breadth = 35
    ticker = 5
elif arguements == 3:
    height = int(sys.argv[1])
    breadth = int(sys.argv[2])
    ticker = 5
elif arguements == 4:
    height = int(sys.argv[1])
    breadth = int(sys.argv[2])
    ticker = int(sys.argv[3])

bitmap = [[0] * breadth for i in range(height)]
bitmap[height // 2][breadth // 2] = 1

currentpropagator = blue_cells

dale = cellularAutomaton(bitmap, currentpropagator)

side = 10
pygame.init()
screensize = [dale.length * side, dale.breadth * side]
screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()

going = True
paused = False
while going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # pause
                paused = not paused

            if event.key == pygame.K_s and paused:
                # save to file
                dale.savefile_handler("mapsv.txt")

            if event.key == pygame.K_l and paused:
                # read from file
                dale.read_saved("mapsv.txt")

    if not paused:
        dale.propagate()

    screen.fill((0, 0, 0))
    for i in range(height):
        for j in range(breadth):
            pygame.draw.rect(screen, (0, dale.cell(i, j) // 2, dale.cell(i, j)), pygame.Rect(i * side, j * side, side - 1, side - 1), 0)

    pygame.display.flip()
    clock.tick(ticker)
