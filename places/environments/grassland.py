from ..environment import Environment

class Grassland(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        try:
            if animal.terrestrial:
                try:
                    if len(self.animals) < 22:
                        self.animals.append(animal)
                except ValueError:
                    print("****   That biome is not large enough   ****")
                    print("****     Please choose another one      ****")
                    raise
        except AttributeError:
            print("****  Only terrestrial animals allowed  ****")
            print("****    Please choose another biome     ****")
            raise

    def add_plant(self, plant):
        try:
            if plant.sunlight is "Full" or plant.req_rainfall is False:
                try:
                    if len(self.plants) < 15:
                        self.plants.append(plant)
                except ValueError:
                    print("****   That biome is not large enough   ****")
                    print("****     Please choose another one      ****")
                    raise
        except AttributeError:
            print("****     Full sunlight plants only      ****")
            print("****    Please choose another biome     ****")
            raise