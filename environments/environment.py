class Environment(Identifiable):
    def __init__(self, name):
        self.animals = []
        self.plants = []
        self.name = name
        Identifiable.__init__(self)

    def __str__(self):
        return self.name