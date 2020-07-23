from animals import Animal
from ..movements import Walking
from ..habitats import Terrestrial

class HawaiianHappyFaceSpider(Animal, Walking, Terrestrial):

    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy-Face Spider")
        Identifiable.__init__(self)
        self.__prey = { "Fly", "Mosquito", "Ant", "Beetle", "Termite" }
        self.minimum_age = 0.5

    def __str__(self):
        return f'{self.species} {self.id}. (8.8)!!'