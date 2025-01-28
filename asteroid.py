from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        vec_1 = pygame.math.Vector2.rotate(self.velocity, angle)
        vec_2 = pygame.math.Vector2.rotate(self.velocity, -angle)

        radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, radius)

        asteroid_1.velocity = vec_1 * 1.2
        asteroid_2.velocity = vec_2 * 1.2
