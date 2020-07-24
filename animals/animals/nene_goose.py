from .animal import Animal
from ..movements import Walking
from ..movements import Swimming
from ..movements import Flying
from ..habitats import Terrestrial

class NeneGoose(Animal, Walking, Swimming, Flying, Terrestrial):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        Walking.__init__(self)
        Swimming.__init__(self)
        Flying.__init__(self)
        Terrestrial.__init__(self)
        self.__prey = { "Plant" }
        self.minimum_age = 7

    def feed(self, prey):
        if prey in self.__prey:
            print(f'{self.species} ate {prey} for a meal')
        else:
            print(f'The {self.species} rejects the {prey}')

    @property
    def prey(self):
        return self.__prey

    def __str__(self):
        return f'{self.species} {self.id}. Honk honk!'