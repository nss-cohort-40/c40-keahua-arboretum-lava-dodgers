from ..environment import Environment

class Swamp(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        try:
            if animal.aquatic and not animal.requires_current:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or non-stagnant water animals to a swamp.")