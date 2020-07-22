from animals import Animal
from animals import Identifiable

class Pueo(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        Identifiable.__init__(self)
        self.__prey = { "Mouse", "Rat" }

    def __str__(self):
        return f'{self.species} {self.id}. eeERREeooooAW!!'