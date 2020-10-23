from app.models.maze import Maze
from app.models.player import Player
from app.models.items import Items

class Game:
    """Class defining game logics."""

    def __init__(self):
        self.maze = Maze()
        self.player = Player(self.maze)
        self.item_ether = Items(self.maze, "e")
        self.item_needle = Items(self.maze, "n")
        self.item_tube = Items(self.maze, "t")

        self.is_running = True
        self.is_end = False
        self.status = "pending"

        self.chars = {"macgyver": "m", "guardian": "g", "ether": "e", "needle": "n", "tube": "t", "wall": "w", "floor": " "}
        self.commands = {"z": "up", "s": "down", "q": "left", "d": "right"}

    def update(self, control):
        if self.status == "pending":
            if control == "up":
                if (self.player.x > 0) and self.maze.structure[self.player.x-1][self.player.y] != "w":
                    self.player.x -= 1
            elif control == "down":
                if (self.player.x < self.maze.size-1) and self.maze.structure[self.player.x+1][self.player.y] != "w":
                    self.player.x += 1
            elif control == "left":
                if (self.player.y > 0) and self.maze.structure[self.player.x][self.player.y-1] != "w":
                    self.player.y -= 1
            elif control == "right":
                if (self.player.y < self.maze.size-1) and self.maze.structure[self.player.x][self.player.y+1] != "w":
                    self.player.y += 1
            elif control == "quit":
                self.is_running = False

            if self.maze.structure[self.player.x][self.player.y] == "e" or \
            self.maze.structure[self.player.x][self.player.y] == "n" or \
            self.maze.structure[self.player.x][self.player.y] == "t":
                self.maze.structure[self.player.x][self.player.y] = " "
                self.player.inventory += 1

            if self.maze.structure[self.player.x][self.player.y] == "g":
                self.is_end = True
                if self.player.inventory == 3:
                    self.status = "win"
                else:
                    self.status = "lose"