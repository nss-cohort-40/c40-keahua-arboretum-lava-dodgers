from .animal import Animal
from ..movements import Walking
from ..movements import Flying
from ..habitats import Terrestrial

class Pueo(Animal, Walking, Flying, Terrestrial):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        Identifiable.__init__(self)
        self.__prey = { "Mouse", "Rat" }
        self.minimum_age = 8

    def __str__(self):
        return f'{self.species} {self.id}. eeERREeooooAW!!'