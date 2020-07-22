from animals import Animal
from animals import Freshwater
from animals import Identifiable

class NeneGoose(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        Freshwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Plant" }

    def __str__(self):
        return f'{self.species} {self.id}. Honk honk!'