class CLIController:
    def __init__(self, game):
        self.game = game
        self.size = self.game.size
        self.structure = self.game.structure
        self.x = 7
        self.y = 0

    def handle_control(self, move):
        if move == "z":
            if (self.y > 0) and self.structure[self.x][self.y-1] != "w":
                self.y -= 1
        elif move == "s":
            if (self.y < self.size-1) and self.structure[self.x][self.y+1] != "w":
                self.y += 1
        elif move == "q":
            if (self.x > 0) and self.structure[self.x-1][self.y] != "w":
                self.x -= 1
        elif move == "d":
            if (self.x < self.size-1) and self.structure[self.x+1][self.y] != "w":
                self.x += 1

        if self.structure[self.x][self.y] == "g":
            print("You won !")