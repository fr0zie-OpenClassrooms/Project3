import pygame
import time

class PygameView:
    def __init__(self, game):
        pygame.init()

        self.game = game
        self.sprite_size = 40
        self.window_width = 600
        self.window_height = 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height + 100))
        self.background_image = pygame.image.load("assets/floor.png").convert()
        self.background = pygame.transform.scale(self.background_image, (self.window_width, self.window_height + 100))

    def display(self):
        macgyver = pygame.image.load("assets/macgyver.png").convert()
        guardian = pygame.image.load("assets/guardian.png").convert()
        ether = pygame.image.load("assets/ether.png").convert()
        needle = pygame.image.load("assets/needle.png").convert()
        tube = pygame.image.load("assets/tube.png").convert()
        wall = pygame.image.load("assets/wall.png").convert()
        floor = pygame.image.load("assets/floor.png").convert()

        pygame.display.set_caption("Help MacGyver to escape !\n")
        self.window.blit(self.background, (0, 0))

        white = (255, 255, 255)
        font = pygame.font.SysFont("lato", 24)

        rule1 = font.render("Pick up all the items and reach the Guardian.", True, white)
        rule2 = font.render("If you try to escape without all the items, you will lose!", True, white)
        inventory = font.render("Inventory: " + str(self.game.player.inventory) + " / 3 items", True, white)
        
        self.window.blit(rule1, (20, 620))
        self.window.blit(rule2, (20, 640))
        self.window.blit(inventory, (20, 660))

        for x in range(self.game.maze.size):
            for y in range(self.game.maze.size):
                x_draw, y_draw = x * self.sprite_size, y * self.sprite_size
                if x == self.game.player.x and y == self.game.player.y:
                    self.window.blit(macgyver, (y_draw, x_draw))
                elif self.game.maze.structure[x][y] == "g":
                    self.window.blit(guardian, (y_draw, x_draw))
                elif self.game.maze.structure[x][y] == "e":
                    self.window.blit(ether, (y_draw, x_draw))
                elif self.game.maze.structure[x][y] == "n":
                    self.window.blit(needle, (y_draw, x_draw))
                elif self.game.maze.structure[x][y] == "t":
                    self.window.blit(tube, (y_draw, x_draw))
                elif self.game.maze.structure[x][y] == "w":
                    self.window.blit(wall, (y_draw, x_draw))
                else:
                    self.window.blit(floor, (y_draw, x_draw))

        pygame.display.update()

        if self.game.at_the_end:
            font = pygame.font.SysFont("lato", 48)
            if self.game.status == "win":
                text = font.render("You won !", True, white)
            elif self.game.status == "lose":
                text = font.render("You lost ! You only had " + str(self.game.player.inventory) + " / 3 items.", True, white)

            text_location = text.get_rect(center=(self.window_width/2, self.window_height/2))
            self.window.blit(text, text_location)
            pygame.display.update()
            pygame.time.delay(3000)
            self.game.is_running = False