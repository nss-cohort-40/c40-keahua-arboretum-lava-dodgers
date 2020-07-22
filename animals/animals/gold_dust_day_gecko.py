from animals import Animal
from ..movements import Walking
from ..habitats import Terrestrial

class GoldDustDayGecko(Animal, Walking, Terrestrial):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        Identifiable.__init__(self)
        self.__prey = { "Fly", "Mosquito", "Ant", "Beetle", "Termite" }

    def __str__(self):
        return f'{self.species} {self.id}. (0.0)!!'