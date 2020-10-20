import sys

from classes.models.maze import Maze
from classes.models.player import Player
from classes.models.items import Items

class Game:
    """Class defining game logics."""

    def __init__(self):
        self.maze = Maze()
        self.size = self.maze.size
        self.structure = self.maze.generate()

    def update(self, control):
        # bouger le hero si le control est un control de mouvement
        # vérifier si le hero est sur un item
        # vérifier si on est sur le gardien.
        pass

    #def __init__(self):
    #    pygame.init()
    #    self.game = pygame.display.set_mode((600, 600))
    #    self.maze = Maze()
    #    self.player = Player(self.maze, 7, 0)
    #    self.item_ether = Items(self.maze, 3, 'assets/ether.png')
    #    self.item_needle = Items(self.maze, 4, 'assets/needle.png')
    #    self.item_tube = Items(self.maze, 5, 'assets/tube.png')
    #    self.floor = pygame.image.load('assets/tile.png').convert()
    #    self.is_over = False

    #def start(self):
    #    """Method to start a new game."""
        # Set title
    #    pygame.display.set_caption("Aidez MacGyver à s'échapper !")
        # Draw items in maze
    #    self.item_ether.draw(self.game)
    #    self.item_needle.draw(self.game)
    #    self.item_tube.draw(self.game)
        # Draw the maze structure and places the player
    #    self.maze.draw(self.game)
    #    self.player.draw(self.game)

    #    pygame.key.set_repeat(200, 30)

        # Game loop
    #    while not self.is_over:
    #        for event in pygame.event.get():
    #            if event.type == QUIT:
    #                self.is_over = True
    #            elif event.type == KEYDOWN:
    #                if event.key == K_UP:
    #                    self.player.moveUp()
    #                elif event.key == K_DOWN:
    #                    self.player.moveDown()
    #                elif event.key == K_LEFT:
    #                    self.player.moveLeft()
    #                elif event.key == K_RIGHT:
    #                    self.player.moveRight()
    #                elif event.key == K_ESCAPE:
    #                    self.is_over = True

            # Draw player at its new location
    #        self.maze.draw(self.game)
    #        self.game.blit(self.player.image, (self.player.x_pos, self.player.y_pos))
    #        pygame.display.flip()

            # Check if player get an item
    #        if (self.maze.structure[self.player.x][self.player.y] == 3) or (self.maze.structure[self.player.x][self.player.y] == 4) or (self.maze.structure[self.player.x][self.player.y] == 5):
    #            self.maze.structure[self.player.x][self.player.y] = 0
    #            self.game.blit(self.floor, (self.player.x_pos, self.player.y_pos))
    #            print('Player got item in', (self.player.x, self.player.y))
    #            self.player.item_list += 1

            # Check if player is on the guardian
    #        if self.maze.structure[self.player.x][self.player.y] == 2:
    #            self.is_over = True

    #def end(self):
    #    while self.is_over:
    #        if self.player.item_list == 3:
    #            print('You won !')
    #            sys.exit(0)
    #        else:
    #            print('You lost !')
    #            sys.exit(0)