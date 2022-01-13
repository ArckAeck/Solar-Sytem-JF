import pygame
import math

white = (255, 255, 255)


class planetstats:
    def __init__(self, screen, length, name, radius, colour, speed, xpos, ypos, xcentre, ycentre, angle, orbit):
        self.screen = screen
        self.length = length
        self.name = name
        self.radius = radius
        self.colour = colour
        self.speed = speed
        self.xpos = 550 + self.length
        self.ypos = 248
        self.xcentre = xcentre
        self.ycentre = ycentre
        self.angle = angle
        self.orbit = self.angle + 100

    def drawplanetboi(self):
        self.movement()
        pygame.draw.circle(self.screen, white, [500, 250], self.length, 1)
        pygame.draw.circle(self.screen, self.colour, [self.x, self.y], self.radius)

    def movement(self):
        self.angle += self.speed / 5000
        xchange = math.sin(self.angle) * self.length
        ychange = math.cos(self.angle) * self.length
        self.x = xchange + self.xcentre
        self.y = ychange + self.ycentre

    def speedup(self):
        self.speed += 20

    def slowdown(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def bigger(self):
        self.radius += 3

    def smaller(self):
        self.radius += -3


