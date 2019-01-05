#!/usr/bin/python3
from partickle import *

def drawparticle(particle, screen):
    particleRect = pygame.Rect(math.floor(particle.position[0]), math.floor(particle.position[1]), particle.size, particle.size)
    pygame.draw.rect(screen, particle.color, particleRect, 0)

size = 500
# one unit time per iteration
dt = 1

caught_count = 0

pygame.init()
screensize = [size, size]
screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()
pygame.display.set_caption("N body: Witness the power of OOP: Encapsulation! Polymorphism! More Stuff for Interviews!")

# the rectangle which represents screen
screenrect = pygame.Rect(0, 0, size, size)

spawnrange = size - 100
running = True

system = []
mass = 1
velocity = [0, 0]
acceleration = [0, 0]
color = (100, 100, 255)
position = [0, 0]
for i in range(0, size, 25):
    for j in range(0, size, 25):
        position[0] = i
        position[1] = j
        x = partickle(mass, position, velocity, acceleration, 2, color)
        system.append(x)

attractors = []
player = partickle(10, [(size / 2), (size / 2)], [0, 0], [0, 0], 5, (200, 200, 200))
attractors.append(player)

screen.fill((0, 0, 0))
for i in range(len(system)):
    drawparticle(system[i], screen)
pygame.display.flip()

while running:
    # function call necessary for getting all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    acc = [0, 0]
    if keys[pygame.K_UP]:
        acc[1] = (-1)

    if keys[pygame.K_DOWN]:
        acc[1] = 1

    if keys[pygame.K_LEFT]:
        acc[0] = (-1)

    if keys[pygame.K_RIGHT]:
        acc[0] = 1

    attractors[0].control(acc)

    for i in range(len(system)):
        system[i].update(attractors, screenrect)

    attractors[0].updatePlayer()

    screen.fill((0, 0, 0))

    for i in range(len(system)):
        drawparticle(system[i], screen)

    for i in range(len(attractors)):
        drawparticle(attractors[i], screen)

    # don't know what this does, exactly
    pygame.display.flip()

    # wait- otherwise the box runs out of the screen- too many key presses
    clock.tick(3)

