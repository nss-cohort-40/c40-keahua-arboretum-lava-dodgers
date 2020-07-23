from .animal import Animal
from ..movements import Swimming
from ..habitats import Freshwater

class Kikakapu(Animal, Swimming, Freshwater):

    def __init__(self):
        Animal.__init__(self, "Kīkākapu")
        Freshwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }
        self.minimum_age = 1

    def __str__(self):
        return f'{self.species} {self.id}. Blurbleblurble!'