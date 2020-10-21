class CLIView:
    def __init__(self, game):
        self.game = game

    def display(self):
        print("\n" * 100)
        print("Help MacGyver (M) to escape !\n")
        print("Controls:\n")
        print("   Z")
        print("Q  S  D\n")
        print("Pick up all the items (I) and reach the Guardian (G).")
        print("If you try to escape without all the items, you will lose!\n")
        print("Inventory:", self.game.player.inventory, "/ 3 items\n")

        for x in range(self.game.maze.size):
            sprite = ""
            for y in range(self.game.maze.size):
                if x == self.game.player.x and y == self.game.player.y:
                    sprite += " M "
                elif self.game.maze.structure[x][y] == "g":
                    sprite += " G "
                elif self.game.maze.structure[x][y] == "e" or \
                     self.game.maze.structure[x][y] == "n" or \
                     self.game.maze.structure[x][y] == "t":
                    sprite += " I "
                elif self.game.maze.structure[x][y] == "w":
                    sprite += "###"
                else:
                    sprite += "   "
            print(sprite)

        if self.game.at_the_end:
            if self.game.status == "win":
                text = "\nYou won !\nPress any key to continue..."
            elif self.game.status == "lose":
                text = "\nYou lost ! You only had " + str(self.game.player.inventory) + " / 3 items.\nPress any key to continue..."

            print(text)
            self.game.is_running = False