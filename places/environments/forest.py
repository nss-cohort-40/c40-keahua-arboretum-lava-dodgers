from ..environment import Environment

class Forest(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        try:
            if animal.terrestrial:
                try:
                    if len(self.animals) < 20:
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
            if plant.sunlight is "Shade" and plant.req_rainfall:
                try:
                    if len(self.plants) < 32:
                        self.plants.append(plant)
                except ValueError:
                    print("****   That biome is not large enough   ****")
                    print("****     Please choose another one      ****")
                    raise
        except AttributeError:
            print("****  Shaded plants requiring rainfall  ****")
            print("****    Please choose another biome     ****")
            raise