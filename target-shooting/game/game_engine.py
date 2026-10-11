"""
GameEngine: owns the targets and handles player clicks.
"""

import random

from game.target import Target
from game.hit_detection import check_hit
from game.renderer import WIDTH, HEIGHT

NUM_TARGETS = 3
TARGET_RADIUS = 28
ROUND_DURATION = 30


class GameEngine:
    def __init__(self):
        self.targets = []
        self.score = 0
        self.combo = 1
        self.hits = 0
        self.misses = 0
        self.time_left = ROUND_DURATION
        self.round_active = True
        self.start_new_round()

    def _random_target(self):
        x = random.randint(TARGET_RADIUS + 10, WIDTH - TARGET_RADIUS - 10)
        y = random.randint(TARGET_RADIUS + 10, HEIGHT - TARGET_RADIUS - 10)
        return Target(x, y, radius=TARGET_RADIUS)

    def start_new_round(self):
        self.targets = [self._random_target() for _ in range(NUM_TARGETS)]
        self.score = 0
        self.combo = 1
        self.hits = 0
        self.misses = 0
        self.time_left = ROUND_DURATION
        self.round_active = True

    def handle_click(self, pos):
        if not self.round_active:
            return

        target = check_hit(self.targets, pos)
        if target is not None:
            self.hits += 1
            self.score += 10 * self.combo
            self.combo += 1
            self.targets.remove(target)
            self.targets.append(self._random_target())
        else:
            self.misses += 1
            self.combo = 1

    def update(self, dt=1 / 60):
        if not self.round_active:
            return

        self.time_left = max(0.0, self.time_left - dt)
        for target in self.targets:
            target.move(WIDTH, HEIGHT)

        if self.time_left <= 0:
            self.time_left = 0.0
            self.round_active = False

    def draw(self, surface, font):
        from game import renderer
        renderer.draw_scene(surface, self.targets)
        renderer.draw_text(surface, font, f"Score: {self.score}  Combo: x{self.combo}", (10, 10))
        renderer.draw_text(surface, font, f"Hits: {self.hits}  Misses: {self.misses}", (10, 40))
        renderer.draw_text(surface, font, f"Time: {self.time_left:.1f}s", (10, 70))

        if not self.round_active:
            renderer.draw_banner(surface, font, f"Final Score: {self.score}")
            renderer.draw_text(surface, font, "Press R to restart", (surface.get_width() // 2 - 80, surface.get_height() // 2 + 40))
