from ..environment import Environment

class Coastline(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        try:
            if animal.terrestrial or animal.flying and not animal.aquatic:
                self.animals.append(animal)
        except AttributeError:
            print("Cannot add aquatic animals to coastline. Put them in the water!")
            raise

    def add_plant(self, plant):
        try:
            if not plant.freshwater and not plant.saltwater:
                if len(self.plants) < 3:
                    self.plants.append(plant)
                else:
                    raise
        except AttributeError:
            print("Cannot add plants that live in the water to coastlines. Put them in the water instead!")
            raise