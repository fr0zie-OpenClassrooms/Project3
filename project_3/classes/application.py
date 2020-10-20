from classes.controllers.cli import CLIController
from classes.controllers.pygame import PygameController
from classes.views.cli import CLIView
from classes.views.pygame import PygameView
from classes.models.game import Game

class Application:
    def __init__(self, output):
        self.game = Game()

        if output == "cli":
            self.view = CLIView(self.game)
            self.controller = CLIController(self.game)
        #else:
        #    self.view = PygameView(self.game)
        #    self.controller = PygameController(self.game)

    def run(self):
        running = True
        while running:
            self.view.display()
            control = self.controller.handle_control()
            self.game.update(control)