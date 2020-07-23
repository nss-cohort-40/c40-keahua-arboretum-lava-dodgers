from .animal import Animal
from ..movements import Flying
from ..habitats import Terrestrial

class Opeapea(Animal, Flying, Terrestrial):

    def __init__(self):
        Animal.__init__(self, "Ope'ape'a")
        Identifiable.__init__(self)
        self.__prey = { "Moth", "Beetle", "Termite" }
        self.minimum_age = 5

    def __str__(self):
        return f'{self.species} {self.id}. Cleek cleek!!'