from animals import Animal

class Pueo(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.__prey = {"Mouse", "Rat"}

    def __str__(self):
        return f'{self.species} {self.id}. eeERREeooooAW!!'