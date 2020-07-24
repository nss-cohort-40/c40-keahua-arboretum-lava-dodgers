from .animal import Animal
from ..movements import Walking
from ..habitats import Terrestrial

class HappyFaceSpider(Animal, Walking, Terrestrial):

    def __init__(self):
        Animal.__init__(self, "Happy-Face Spider")
        Walking.__init__(self)
        Terrestrial.__init__(self)
        self.__prey = { "Fly", "Mosquito", "Ant", "Beetle", "Termite" }
        self.minimum_age = 0.5
        
    def feed(self, prey):
        if prey in self.__prey:
            print(f'{self.species} ate {prey} for a meal')
        else:
            print(f'The {self.species} rejects the {prey}')

    @property
    def prey(self):
        return self.__prey

    def __str__(self):
        return f'{self.species} {self.id}. (8.8)!!'