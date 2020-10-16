import pygame

class Player:
    """Class creating the player's character."""

    def __init__(self, maze, x, y):
        self.maze = maze
        self.image = pygame.image.load('assets/macgyver.png').convert_alpha()
        self.item_list = 0
        self.x = x
        self.y = y
        self.x_pos = x * 40
        self.y_pos = y * 40

    def moveUp(self):
        """Method used when the player go up."""

        # Check if player is not at the edge
        if self.y > 0:
            # Check if it's not a wall
            if self.maze.structure[self.y-1][self.x] != 1:
                self.y -= 1
                self.y_pos = self.y * 40

    def moveDown(self):
        """Method used when the player go down."""

        # Check if player is not at the edge
        if self.y < 14:
            # Check if it's not a wall
            if self.maze.structure[self.y+1][self.x] != 1:
                self.y += 1
                self.y_pos = self.y * 40

    def moveLeft(self):
        """Method used when the player go left."""

        # Check if player is not at the edge
        if self.x > 0:
            # Check if it's not a wall
            if self.maze.structure[self.y][self.x-1] != 1:
                self.x -= 1
                self.x_pos = self.x * 40
    
    def moveRight(self):
        """Method used when the player go right."""

        # Check if player is not at the edge
        if self.x < 14:
            # Check if it's not a wall
            if self.maze.structure[self.y][self.x+1] != 1:
                self.x += 1
                self.x_pos = self.x * 40

    def draw(self, game):
        """Method used to draw the player at its location."""

        game.blit(self.image, (self.x_pos, self.y_pos))