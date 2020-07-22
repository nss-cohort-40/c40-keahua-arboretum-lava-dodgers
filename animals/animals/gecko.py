from animals import Animal
from animals import Identifiable

class GoldDustDayGecko(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        Identifiable.__init__(self)
        self.__prey = { "Fly", "Mosquito", "Ant", "Beetle", "Termite" }

    def __str__(self):
        return f'{self.species} {self.id}. (0.0)!!'