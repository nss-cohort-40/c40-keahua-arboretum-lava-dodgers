from misc import Identifiable

class Environment(Identifiable):
    def __init__(self, name):
        self.animals = []
        self.plants = []
        self.name = name
        Identifiable.__init__(self)

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it"
    
    def plant_count(self):
        return f"This place has {len(self.plants)} animals in it"

    def __str__(self):
        return self.name