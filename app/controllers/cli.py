class CLIController:
    """Class defining terminal controller."""

    def __init__(self, game):
        """Class initialization."""

        self.game = game

    def handle_control(self):
        """Method used to get player's keyboard capture."""

        commands = self.game.commands
        control = input()
        
        if control in commands:
            return commands[control]