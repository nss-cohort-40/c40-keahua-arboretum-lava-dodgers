from .animal import Animal
from ..movements import Walking
from ..movements import Swimming
from ..movements import Flying
from ..habitats import Terrestrial

class NeneGoose(Animal, Walking, Swimming, Flying, Terrestrial):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        self.__prey = { "Plant" }
        self.minimum_age = 7

    def __str__(self):
        return f'{self.species} {self.id}. Honk honk!'