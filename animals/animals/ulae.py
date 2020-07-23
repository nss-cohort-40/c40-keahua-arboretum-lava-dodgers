from .animal import Animal
from ..movements import Swimming
from ..habitats import Saltwater

class Ulae(Animal, Swimming, Saltwater):

    def __init__(self):
        Animal.__init__(self, "'Ulae")
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }
        self.minimum_age = 1

    def __str__(self):
        return f'{self.species} {self.id}. Blurbleblurble!!'