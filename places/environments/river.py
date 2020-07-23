from ..environment import Environment

class River(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            print("Cannot add non-aquatic, or saltwater animals to a river")
            raise

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            print("Cannot add plants that require brackish water or stagnant water to a river biome")
            raise