import pygame
import random
from constants import *
from circleshape import *

class Astroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_angle_1 = self.velocity.rotate(angle)
            new_angle_2 = self.velocity.rotate(angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_one = Astroid(self.position.x, self.position.y, new_radius)
            new_two = Astroid(self.position.x, self.position.y, new_radius)
            new_one.velocity += new_angle_1 * 1.2
            new_two.velocity += new_angle_2 * 1.2

            print(f"{new_angle_1}, {new_angle_2}, {new_radius}")

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt