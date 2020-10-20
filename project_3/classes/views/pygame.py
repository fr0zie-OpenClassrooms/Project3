class PygameView:
    def display(self, game):
        """Method used to draw the maze structure (walls, path, guardian location) within the 'game' window."""

        size = 40
        wall = pygame.image.load('assets/wall.png').convert()
        floor = pygame.image.load('assets/tile.png').convert()
        guardian = pygame.image.load('assets/guardian.png').convert()

        row_nb = 0
        for row in self.structure:
            column_nb = 0
            for column in row:
                x = column_nb * size
                y = row_nb * size
                if column == 0:
                    game.blit(floor, (x, y))
                elif column == 1:
                    game.blit(wall, (x, y))
                elif column == 2:
                    game.blit(guardian, (x, y))
                column_nb += 1
            row_nb += 1             

if __name__ == "__main__":
    CLIView("maze.txt")