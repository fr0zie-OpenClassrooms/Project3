import pygame
from pygame.locals import K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN, KEYDOWN, QUIT

from classes.models.maze import Maze

class PygameController:
    def __init__(self):
        self.x = 7
        self.y = 0
        self.maze = Maze("maze.txt")
        self.structure = self.maze.generate()

    def handle_control(self, move):
        if move == "z":
            if (self.y > 0) and self.structure[self.x][self.y-1] != "w":
                self.y -= 1
        elif move == "s":
            if (self.y < self.maze.size-1) and self.structure[self.x][self.y+1] != "w":
                self.y += 1
        elif move == "q":
            if (self.x > 0) and self.structure[self.x-1][self.y] != "w":
                self.x -= 1
        elif move == "d":
            if (self.x < self.maze.size-1) and self.structure[self.x+1][self.y] != "w":
                self.x += 1