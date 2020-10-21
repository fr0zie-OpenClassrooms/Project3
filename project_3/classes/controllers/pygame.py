import pygame
from pygame.locals import K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN, KEYDOWN, QUIT

class PygameController:
    def __init__(self, game):
        self.game = game

    def handle_control(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    return "z"
                elif event.key == K_DOWN:
                    return "s"
                elif event.key == K_LEFT:
                    return "q"
                elif event.key == K_RIGHT:
                    return "d"
                elif event.key == K_ESCAPE:
                    return "quit"