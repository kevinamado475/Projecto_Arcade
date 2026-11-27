# importa Random para que cualquier cosa 
import random


class robot:
    name = "machine"
    game = ["pedra","paper","tisora"]  # noqa: RUF012

    def playing(self):
        choice = random.choice(self.game)
        return choice
