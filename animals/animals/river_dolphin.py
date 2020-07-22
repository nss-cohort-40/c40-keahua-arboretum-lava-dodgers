from animals import Animal
from animals import Freshwater
from animals import Identifiable

class RiverDolphin(Animal, Freshwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "River dolphin")
        Freshwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }

    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
