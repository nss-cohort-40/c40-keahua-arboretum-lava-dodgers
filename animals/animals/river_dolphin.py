from animals import Animal
from ..movements import Swimming
from ..habitats import Freshwater

class RiverDolphin(Animal, Swimming, Freshwater):

    def __init__(self):
        Animal.__init__(self, "River dolphin")
        Freshwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }
        self.minimum_age = 13

    def __str__(self):
        return f'{self.species} {self.id}. Eeee EeeEEeeeeEE!'
