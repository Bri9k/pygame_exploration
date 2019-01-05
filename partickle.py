import pygame
import math

PLAYER = 1
UNLIVING = 0
COUNT = 0
G = 1
dt = 1
DIMENSION = 2


def init(constant, timestep, dimension):
    global G, dt, DIMENSION
    G = constant
    dt = timestep
    DIMENSION = dimension

class partickle:
    # constructor
    def __init__(self, mass, position, velocity, acceleration, size, color):
        global DIMENSION, COUNT
        self.mass = mass
        self.position = [position[0], position[1]]
        self.velocity = [velocity[0], velocity[1]]
        self.acceleration = [acceleration[0], acceleration[1]]
        self.size = size
        self.color = color

        # for uniqueness
        self.ID = COUNT
        COUNT += 1

    def update(self, system, boundingRect):
        global DIMENSION
        total_force = [0 for i in range(DIMENSION)]
        for i in range(len(system)):
            # body does not exert force on itself
            if system[i].ID == self.ID:
                continue

            # compute particle to current object vector
            r = [system[0].position[0] - self.position[0], system[i].position[1] - self.position[1]]

            dist = 0
            for j in range(DIMENSION):
                dist += r[j] * r[j]

            dist = math.sqrt(dist)

            if dist < 0.0001:
                dist = 1

            force_magnitude = G * self.mass * system[i].mass / (dist) #* dist)

            force = [force_magnitude * r[j] / dist for j in range(DIMENSION)]
            force[0] = force_magnitude * r[0] / dist
            force[1] = force_magnitude * r[1] / dist
            
            # update force
            total_force[0] += force[0]
            total_force[1] += force[1]

            # kinemetics
            for j in range(2):
                self.acceleration[j] += total_force[j] / self.mass
                self.velocity[j] += self.acceleration[j] * dt
                self.position[j] += self.velocity[j] * dt + 0.5 * self.acceleration[j] * dt * dt

        self_rect = pygame.Rect(self.position[0], self.position[0], self.size, self.size)

        #if not boundingRect.contains(self_rect):
        #    self.velocity[0] = -self.velocity[0]
        #    self.velocity[1] = -self.velocity[1]



    def updatePlayer(self):
        for j in range(2):
            self.velocity[j] += self.acceleration[j] * dt
            self.position[j] += self.velocity[j] * dt + 0.5 * self.acceleration[j] * dt * dt



    def control(self, acc_incr):
        self.acceleration[0] = acc_incr[0]
        self.acceleration[1] = acc_incr[1]



