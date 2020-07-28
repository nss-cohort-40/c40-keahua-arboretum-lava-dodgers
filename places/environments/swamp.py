from ..environment import Environment

class Swamp(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        try:
            if animal.species == "Happy-Face Spider" or animal.cell_type == "hypertonic":
                try:
                    if len(self.animals) < 8:
                        self.animals.append(animal)
                except ValueError:
                    print("****   That biome is not large enough   ****")
                    print("****     Please choose another one      ****")
        except AttributeError:
            print("****  Only stagnant freshwater animals allowed  ****")
            print("****        Please choose another biome         ****")

    def add_plant(self, plant):
        try:
            if plant.req_freshwater and not plant.req_current:
                try:
                    if len(self.plants) < 12:
                        self.plants.append(plant)
                except ValueError:
                    print("****   That biome is not large enough   ****")
                    print("****     Please choose another one      ****")
        except AttributeError:
            print("****   Only moving freshwater plants allowed   ****")
            print("****        Please choose another biome        ****")
