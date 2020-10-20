class Maze:
    """Class defining maze structure."""

    def __init__(self, file="maze.txt", size=15):
        """Method that initializes the maze with its structure."""

        self.file = file
        self.size = size
        self.structure = []

    def generate(self):
        """Generates the maze based on the map file."""

        with open(self.file) as file:
            maze_structure = []
            for rows in file:
                maze_row = []
                for sprite in rows:
                    if sprite != "\n":
                        maze_row.append(sprite)
                maze_structure.append(maze_row)
            self.structure = maze_structure