import pygame
from pygame.locals import K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN, KEYDOWN, QUIT

class PygameController:
    def __init__(self, game):
        self.game = game

    def handle_control(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return "quit"
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    return "up"
                elif event.key == K_DOWN:
                    return "down"
                elif event.key == K_LEFT:
                    return "left"
                elif event.key == K_RIGHT:
                    return "right"
                elif event.key == K_ESCAPE:
                    return "quit"