from app.models.maze import Maze
from app.models.player import Player
from app.models.items import Items


class Game:
    """Class defining game logics."""

    def __init__(self):
        """Class initialization."""

        self.chars = {
            "start": "s",
            "macgyver": "m",
            "guardian": "g",
            "ether": "e",
            "needle": "n",
            "tube": "t",
            "wall": "w",
            "floor": " "
            }
        self.commands = {"z": "up", "s": "down", "q": "left", "d": "right"}

        self.maze = Maze()
        self.player = Player(self.maze)
        self.item_ether = Items(self.maze, self.chars["ether"])
        self.item_needle = Items(self.maze, self.chars["needle"])
        self.item_tube = Items(self.maze, self.chars["tube"])

        self.is_running = True
        self.is_end = False
        self.status = "pending"

    def update(self, control):
        """Method used to update player movements,
        objects recovery and game end."""

        # If the game is running (neither won nor lost)
        if self.status == "pending":
            # If the player goes up
            if control == "up":
                if self.player.x > 0 and \
                        self.maze.structure[self.player.x-1][self.player.y] != self.chars["wall"]:
                    self.player.x -= 1
            # If the player goes down
            elif control == "down":
                if self.player.x < self.maze.size-1 and \
                        self.maze.structure[self.player.x+1][self.player.y] != self.chars["wall"]:
                    self.player.x += 1
            # If the player goes left
            elif control == "left":
                if self.player.y > 0 and \
                        self.maze.structure[self.player.x][self.player.y-1] != self.chars["wall"]:
                    self.player.y -= 1
            # If the player goes right
            elif control == "right":
                if self.player.y < self.maze.size-1 and \
                        self.maze.structure[self.player.x][self.player.y+1] != self.chars["wall"]:
                    self.player.y += 1
            # If the player stops the game
            elif control == "quit":
                self.is_running = False

            # If the player recovers an item, replace it
            # with a floor and increments inventory.
            if self.maze.structure[self.player.x][self.player.y] == self.chars["ether"] or \
                    self.maze.structure[self.player.x][self.player.y] == self.chars["needle"] or \
                    self.maze.structure[self.player.x][self.player.y] == self.chars["tube"]:
                self.maze.structure[self.player.x][self.player.y] = self.chars["floor"]
                self.player.inventory += 1

            # If the player is on Guardian (game end), check if he has
            # all the objects. If he does, he won. If not, he lost.
            if self.maze.structure[self.player.x][self.player.y] == self.chars["guardian"]:
                self.is_end = True
                if self.player.inventory == 3:
                    self.status = "win"
                else:
                    self.status = "lose"
