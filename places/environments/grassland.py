from ..environment import Environment

class Grassland(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        try:
            if animal.terrestrial:
                self.animals.append(animal)
        except AttributeError:
            print("Cannot add non-terrestrial animal to grasslands, obviously.")
            raise

    def add_plant(self, plant):
        try:
            if not plant.requires_current or not plant.saltwater:
                self.plants.append(plant)
        except AttributeError:
            print("Cannot add plants that require water to grasslands, silly.")
            raise