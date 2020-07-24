from ..environment import Environment

class Mountain(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        try:
            if animal.terrestrial:
                try:
                    if len(self.animals) < 6:
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
            if plant.req_elevation:
                try:
                    if len(self.plants) < 4:
                        self.plants.append(plant)
                except ValueError:
                    print("****   That biome is not large enough   ****")
                    print("****     Please choose another one      ****")
                    raise
        except AttributeError:
            print("****     Aquatic plants disallowed      ****")
            print("****    Please choose another biome     ****")
            raise