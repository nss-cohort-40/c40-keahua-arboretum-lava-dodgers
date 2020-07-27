from ..environment import Environment

class River(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                try:
                    if len(self.animals) < 12:
                        self.animals.append(animal)
                except ValueError:
                    print("****   That biome is not large enough   ****")
                    print("****     Please choose another one      ****")
        except AttributeError:
            print("****  Only freshwater aquatic animals allowed  ****")
            print("****        Please choose another biome        ****")
            input("Press any key to continue >>")
            raise

    def add_plant(self, plant):
        try:
            if plant.req_current and plant.req_freshwater:
                try:
                    if len(self.plants) < 6:
                        self.plants.append(plant)
                except ValueError:
                    print("****   That biome is not large enough   ****")
                    print("****     Please choose another one      ****")
        except AttributeError:
            print("****   Only moving freshwater plants allowed   ****")
            print("****        Please choose another biome        ****")
