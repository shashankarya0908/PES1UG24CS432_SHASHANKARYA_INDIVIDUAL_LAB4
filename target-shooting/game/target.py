"""
Target: a circular target the player clicks on. (x, y) is the CENTER
of the circle - this matters for how it's drawn vs. how it's hit-tested.
"""

import random

import pygame


class Target:
    def __init__(self, x, y, radius=28, color=(230, 90, 70)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = random.uniform(1.5, 3.5) * random.choice((-1, 1))
        self.vy = random.uniform(1.5, 3.5) * random.choice((-1, 1))

    def get_bounding_rect(self):
        """Return the square region enclosing the circle."""
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def move(self, width, height):
        next_x = self.x + self.vx
        next_y = self.y + self.vy

        if next_x - self.radius <= 0 or next_x + self.radius >= width:
            self.vx *= -1
            next_x = max(self.radius, min(next_x, width - self.radius))

        if next_y - self.radius <= 0 or next_y + self.radius >= height:
            self.vy *= -1
            next_y = max(self.radius, min(next_y, height - self.radius))

        self.x = next_x
        self.y = next_y
