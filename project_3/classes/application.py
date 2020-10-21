from classes.controllers.cli import CLIController
from classes.controllers.pygame import PygameController

from classes.views.cli import CLIView
from classes.views.pygame import PygameView

from classes.models.game import Game

class Application:
    def __init__(self, output: str):
        self.game = Game()

        if output == "cli":
            self.view = CLIView(self.game)
            self.controller = CLIController(self.game)
        elif output == "pygame":
            self.view = PygameView(self.game)
            self.controller = PygameController(self.game)

    def run(self):
        while self.game.is_running:
            self.view.display()
            control = self.controller.handle_control()
            self.game.update(control)

        print("Thanks for playing the game!")