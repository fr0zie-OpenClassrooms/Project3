class CLIView:
    def __init__(self, game):
        self.game = game
        self.chars = self.game.chars

    def display(self):
        self.display_text()
        self.display_maze()
        self.display_status()

    def display_maze(self):
        for x in range(self.game.maze.size):
            sprite = ""
            for y in range(self.game.maze.size):
                structure = self.game.maze.structure[x][y]
                
                if x == self.game.player.x and y == self.game.player.y:
                    sprite += " M "
                elif structure == self.chars["guardian"]:
                    sprite += " G "
                elif structure == self.chars["ether"] or \
                     structure == self.chars["needle"] or \
                     structure == self.chars["tube"]:
                    sprite += " I "
                elif structure == self.chars["wall"]:
                    sprite += "###"
                elif structure == self.chars["floor"]:
                    sprite += "   "
            print(sprite)

    def display_text(self):
        print("\n" * 100)
        print("Help MacGyver (M) to escape !\n")
        print("Controls:\n")
        print("   Z")
        print("Q  S  D\n")
        print("Pick up all the items (I) and reach the Guardian (G).")
        print("If you try to escape without all the items, you will lose!\n")
        print(f"Inventory: {str(self.game.player.inventory)}/3 items\n")

    def display_status(self):
        if self.game.is_end:
            if self.game.status == "win":
                text = "\nYou won !\nPress any key to continue..."
            elif self.game.status == "lose":
                text = f"\nYou lost ! You only had {str(self.game.player.inventory)}/3 items.\nPress any key to continue..."

            print(text)
            self.game.is_running = False