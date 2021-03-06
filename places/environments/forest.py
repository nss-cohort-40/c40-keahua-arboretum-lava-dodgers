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
        except AttributeError:
            print("****  Only terrestrial animals allowed  ****")
            print("****    Please choose another biome     ****")

    def add_plant(self, plant):
        try:
            if plant.sunlight == "Shade" and plant.req_rainfall == True:
                try:
                    if len(self.plants) < 32:
                        self.plants.append(plant)
                except ValueError:
                    print("****   That biome is not large enough   ****")
                    print("****     Please choose another one      ****")
        except AttributeError:
            print("****  Shaded plants requiring rainfall  ****")
            print("****    Please choose another biome     ****")
