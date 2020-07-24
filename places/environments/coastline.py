from ..environment import Environment

class Coastline(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypotonic":
                try:
                    if len(self.animals) < 15:
                        self.animals.append(animal)
                except ValueError:
                    print("****   That biome is not large enough   ****")
                    print("****     Please choose another one      ****")
        except AttributeError:
            print("****   Only saltwater animals allowed   ****")
            print("****    Please choose another biome     ****")

    def add_plant(self, plant):
        try:
            if plant.req_saltwater:
                try:
                    if len(self.plants) < 3:
                        self.plants.append(plant)
                except ValueError:
                    print("****   That biome is not large enough   ****")
                    print("****     Please choose another one      ****")
        except AttributeError:
            print("****   Only saltwater plants allowed    ****")
            print("****    Please choose another biome     ****")
