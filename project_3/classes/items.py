import pygame
import random

class Items:
    """Class randomizing items location."""

    def __init__(self, maze, id, image):
        """Method that initializes the item in the specified maze, with its ID and image."""

        self.maze = maze
        self.id = id
        self.image = pygame.image.load(image).convert_alpha()
        self.x, self.y = self.randomize_pos(id)
        self.x_pos = self.x * 40
        self.y_pos = self.y * 40

    def randomize_pos(self, id):
        """Method used in item initialization to randomize its location."""

        # The item in not placed yet
        is_item_placed = False

        # Loop until item is placed
        while not is_item_placed:
            # Randomizes 'x' and 'y' locations within the 15x15 structure
            self.x = random.randint(0, 14)
            self.y = random.randint(0, 14)

            # If location is not a wall, place the item
            if self.maze.structure[self.x][self.y] == 0:
                self.maze.structure[self.x][self.y] = id
                is_item_placed = True

        return self.x, self.y

    def draw(self, game):
        """Method used to draw items in the maze structure within the 'game' window."""

        game.blit(self.image, (self.x_pos, self.y_pos))