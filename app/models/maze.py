class Maze:
    """Class defining maze structure."""

    def __init__(self, file="data/maze.txt", size=15, x=0, y=7):
        """Method that initializes the maze with its structure."""

        self.file = file
        self.size = size
        self.x = x
        self.y = y
        self.structure = self.generate()

    def generate(self):
        """Generates the maze based on the map file."""

        with open(self.file) as file:
            maze_structure = []
            for row in file:
                maze_row = []
                for sprite in row:
                    if sprite != "\n":
                        maze_row.append(sprite)
                maze_structure.append(maze_row)
            
        return maze_structure