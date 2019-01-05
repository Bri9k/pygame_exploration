import pygame
import random

size = 500
# one unit time per iteration
dt = 1

caught_count = 0

pygame.init()
screensize = [size, size]
screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()
time = 0

# the rectangle which represents screen
screenrect = pygame.Rect(0, 0, size, size)

spawnrange = size - 100

pos = [5, 5]
vel = [0, 0]
acc = [0, 0]


running = True
respawn = True
spawn_player = True

pygame.display.set_caption("Pakda Pakdi!. Score: " + str(caught_count))

while running:

    pygame.display.set_caption("Pakda Pakdi!. Score: " + str(caught_count))

    # function call necessary for getting all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # which keys are pressed?
    keys = pygame.key.get_pressed()
    
    # reset acc to 0 everytime
    acc = [0, 0]


    # random location for target position
    if respawn:
        target_pos = [random.randrange(spawnrange), random.randrange(spawnrange)]
        target_vel = [0, 0]
        target_acc = [0, 0]

    if spawn_player:
        pos = [random.randrange(spawnrange) for i in range(2)]

    respawn = False
    spawn_player = False

    if keys[pygame.K_UP]:
        acc[1] += (-1)

    if keys[pygame.K_DOWN]:
        acc[1] += 1

    if keys[pygame.K_LEFT]:
        acc[0] += (-1)

    if keys[pygame.K_RIGHT]:
        acc[0] += 1

    # Integrate!
    for i in range(2):
        target_acc[i] = random.randrange(-1, 2)
        target_vel[i] += target_acc[i]
        target_pos[i] += target_vel[i]
        vel[i] += acc[i] * dt
        pos[i] += vel[i] * dt


    # build the rectangles
    playerRect = pygame.Rect(pos[0], pos[1], 30, 30)
    targetRect = pygame.Rect(target_pos[0], target_pos[1], 20, 20)

    # here a list of objects would be better- for all objects I have to update position and velocity, then draw them on the screen
    
    if  playerRect.colliderect(targetRect):
        caught_count += 1
        respawn = True

    if not screenrect.contains(playerRect):
       spawn_player  = True
 
    if not screenrect.contains(targetRect):
        respawn = True

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (200, 200, 66), playerRect, 0)
    pygame.draw.rect(screen, (42, 100, 100), targetRect, 0)

    # don't know what this does, exactly
    pygame.display.flip()

    # wait- otherwise the box runs out of the screen- too many key presses
    clock.tick(30)

    time += 30 / 1000





