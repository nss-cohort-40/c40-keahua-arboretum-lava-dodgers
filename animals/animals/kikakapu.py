from animals import Animal
from animals import Freshwater
from animals import Identifiable

class Kikakapu(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Kīkākapu")
        Freshwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }

    def __str__(self):
        return f'{self.species} {self.id}. Blurbleblurble!'