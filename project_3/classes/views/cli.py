class CLIView:
    def __init__(self, game):
        self.game = game
        self.structure = self.game.structure

    def display(self):
        for rows in self.structure:
            sprite = ""
            for sprites in rows:
                if sprites == "w":
                    sprite += "###"
                elif sprites == "m":
                    sprite += " M "
                elif sprites == "g":
                    sprite += " G "
                else:
                    sprite += "   "
            print(sprite)