import sys

from classes.models.maze import Maze
from classes.models.player import Player
from classes.models.items import Items

class Game:
    """Class defining game logics."""

    def __init__(self):
        self.maze = Maze()
        self.player = Player(self.maze)
        self.item_ether = Items(self.maze, "e")
        self.item_needle = Items(self.maze, "n")
        self.item_tube = Items(self.maze, "t")

        self.is_running = True

    def update(self, control):
        if control == "z":
            if (self.player.x > 0) and self.maze.structure[self.player.x-1][self.player.y] != "w":
                self.player.x -= 1
        elif control == "s":
            if (self.player.x < self.maze.size-1) and self.maze.structure[self.player.x+1][self.player.y] != "w":
                self.player.x += 1
        elif control == "q":
            if (self.player.y > 0) and self.maze.structure[self.player.x][self.player.y-1] != "w":
                self.player.y -= 1
        elif control == "d":
            if (self.player.y < self.maze.size-1) and self.maze.structure[self.player.x][self.player.y+1] != "w":
                self.player.y += 1

        if self.maze.structure[self.player.x][self.player.y] == "e" or \
        self.maze.structure[self.player.x][self.player.y] == "n" or \
        self.maze.structure[self.player.x][self.player.y] == "t":
            self.maze.structure[self.player.x][self.player.y] = " "
            self.player.inventory += 1

        if self.maze.structure[self.player.x][self.player.y] == "g":
            if self.player.inventory == 3:
                print("You won !")
                self.is_running = False
            else:
                print("You lost !")
                self.is_running = False