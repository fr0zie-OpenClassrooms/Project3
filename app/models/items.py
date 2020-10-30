from random import randint


class Items:
    """Class randomizing items location."""

    def __init__(self, maze, id: str):
        """Method that initializes an item in the specified maze,
        with its ID."""

        self.maze = maze
        self.id = id
        self.x, self.y = self.set_item(id)

    def set_item(self, id):
        """Method used to randomize and set items location."""

        # The item in not placed yet
        is_item_placed = False

        # Loop until item is placed
        while not is_item_placed:
            # Randomizes 'x' and 'y' locations within the 15x15 structure
            self.x = randint(0, self.maze.size-1)
            self.y = randint(0, self.maze.size-1)

            # If location is not a wall, place the item
            if self.maze.structure[self.x][self.y] == " ":
                self.maze.structure[self.x][self.y] = id
                is_item_placed = True

        return self.x, self.y
