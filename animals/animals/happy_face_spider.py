from .animal import Animal
from ..movements import Walking
from ..habitats import Terrestrial

class HappyFaceSpider(Animal, Walking, Terrestrial):

    def __init__(self):
        Animal.__init__(self, "Happy-Face Spider")
        self.__prey = { "Fly", "Mosquito", "Ant", "Beetle", "Termite" }
        self.minimum_age = 0.5

    def __str__(self):
        return f'{self.species} {self.id}. (8.8)!!'