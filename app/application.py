from app.controllers.cli import CLIController
from app.controllers.pygame import PygameController

from app.views.cli import CLIView
from app.views.pygame import PygameView

from app.models.game import Game

class Application:
    """Class used to setup a new game with the chosen output."""

    def __init__(self, output: str):
        """Class initialization."""

        self.game = Game()

        if output == "cli":
            self.view = CLIView(self.game)
            self.controller = CLIController(self.game)
        elif output == "pygame":
            self.view = PygameView(self.game)
            self.controller = PygameController(self.game)

    def run(self):
        """Method used to loop game."""
        
        while self.game.is_running:
            self.view.display()
            control = self.controller.handle_control()
            self.game.update(control)

        print("Thanks for playing the game!")