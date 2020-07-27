from .animal import Animal
from ..movements import Swimming
from ..habitats import Freshwater

class Kikakapu(Animal, Swimming, Freshwater):

    def __init__(self):
        Animal.__init__(self, "Kīkākapu")
        Swimming.__init__(self)
        Freshwater.__init__(self)
        self.__prey = { "Trout", "Mackerel", "Salmon", "Sardine" }
        self.minimum_age = 1

    def feed(self, prey):
        if prey in self.__prey:
            print(f'{self.species} ate {prey} for a meal')
        else:
            print(f'The {self.species} rejects the {prey}')

    @property
    def prey(self):
        return self.__prey
        
    def __str__(self):
        return f'{self.species} {self.id}. Blurbleblurble!'