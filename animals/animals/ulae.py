from animals import Animal
from ..movements import Swimming
from ..habitats import Saltwater

class Ulae(Animal, Swimming, Saltwater):

    def __init__(self):
        Animal.__init__(self, "'Ulae")
        Identifiable.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }

    def __str__(self):
        return f'{self.species} {self.id}. Blurbleblurble!!'