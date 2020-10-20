class CLIController:
    def __init__(self, game):
        self.game = game

    def handle_control(self):
        move = input()
        return move