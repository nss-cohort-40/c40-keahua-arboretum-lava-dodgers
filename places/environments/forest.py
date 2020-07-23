from ..environment import Environment

class Forest(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        try:
            if animal.terrestrial:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-terrestrial animal to forest, obviously.")

    def add_plant(self, plant):
        try:
            if not plant.freshwater and not plant.saltwater:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require water to forests, silly.")