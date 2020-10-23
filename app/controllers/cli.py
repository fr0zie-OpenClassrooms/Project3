class CLIController:
    def __init__(self, game):
        self.game = game

    def handle_control(self):
        commands = self.game.commands
        control = input()
        
        if control in commands:
            return commands[control]