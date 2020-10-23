class Player:
    """Class creating the player's character."""

    def __init__(self, maze):
        self.maze = maze
        self.inventory = 0
        self.x = self.maze.x
        self.y = self.maze.y
