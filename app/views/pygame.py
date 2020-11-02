import pygame


class PygameView:
    """Class defining PyGame view."""

    def __init__(self, game):
        """Class initialization."""

        pygame.init()
        pygame.key.set_repeat(50, 100)

        self.game = game
        self.chars = self.game.chars
        self.sprite_size = 40
        self.window_width = 600
        self.window_height = 600
        self.window = pygame.display.set_mode(
                (self.window_width, self.window_height + 100)
            )
        self.background_image = pygame.image.load("assets/floor.png").convert()
        self.background = pygame.transform.scale(
                self.background_image,
                (self.window_width, self.window_height + 100)
            )
        self.images = {
            "macgyver": pygame.image.load("assets/macgyver.png").convert_alpha(),
            "guardian": pygame.image.load("assets/guardian.png").convert(),
            "ether": pygame.image.load("assets/ether.png").convert(),
            "needle": pygame.image.load("assets/needle.png").convert(),
            "tube": pygame.image.load("assets/tube.png").convert(),
            "wall": pygame.image.load("assets/wall.png").convert(),
            "floor": pygame.image.load("assets/floor.png").convert(),
            }

        self.color_white = (255, 255, 255)
        self.font = pygame.font.SysFont("lato", 24)

        pygame.display.set_caption("Help MacGyver to escape!\n")

    def display(self):
        """Method used to display the whole game before each update."""

        self.window.blit(self.background, (0, 0))

        self.display_text()
        self.display_maze()
        self.display_status()

        pygame.display.update()

    def display_maze(self):
        """Method used to display the maze structure."""

        for y in range(self.game.maze.size):
            for x in range(self.game.maze.size):
                structure = self.game.maze.structure[x][y]
                position = y * self.sprite_size, x * self.sprite_size

                if self.game.player.x == x and self.game.player.y == y:
                    self.window.blit(self.images["macgyver"], position)
                elif structure == self.chars["guardian"]:
                    self.window.blit(self.images["guardian"], position)
                elif structure == self.chars["ether"]:
                    self.window.blit(self.images["ether"], position)
                elif structure == self.chars["needle"]:
                    self.window.blit(self.images["needle"], position)
                elif structure == self.chars["tube"]:
                    self.window.blit(self.images["tube"], position)
                elif structure == self.chars["wall"]:
                    self.window.blit(self.images["wall"], position)
                elif structure == self.chars["floor"] or \
                        structure == self.chars["start"]:
                    self.window.blit(self.images["floor"], position)

    def display_text(self):
        """Method used to display the game text. (rules, inventory)"""

        rule1 = self.font.render(
                "Pick up all the items and reach the Guardian.",
                True, self.color_white)
        rule2 = self.font.render(
                "If you try to escape without all the items, you will lose!",
                True, self.color_white)
        inventory = self.font.render(
            f"Inventory: {str(self.game.player.inventory)}/3 items",
            True, self.color_white)

        self.window.blit(rule1, (20, 620))
        self.window.blit(rule2, (20, 640))
        self.window.blit(inventory, (20, 660))

    def display_status(self):
        """Method used to display the game status
        when player reaches the end."""

        if self.game.is_end:
            self.font = pygame.font.SysFont("lato", 48)
            if self.game.status == "win":
                text = self.font.render("You won !", True, self.color_white)
            elif self.game.status == "lose":
                text = self.font.render(
                    f"You lost ! You only had {str(self.game.player.inventory)}/3 items.",
                    True, self.color_white)

            text_location = text.get_rect(
                    center=(self.window_width/2, self.window_height/2)
                )
            self.window.blit(text, text_location)
            pygame.display.update()
            pygame.time.delay(3000)
            self.game.is_running = False
