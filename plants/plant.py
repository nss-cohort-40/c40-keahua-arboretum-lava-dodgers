from misc import Identifiable

class Plant(Identifiable):

    def __init__(self, species, season, seeds, habitats, resistance, sunlight):
        self.species = species
        self.peak_season = season
        self.seeds_produced = seeds
        self.hospitable = habitats
        self.insecticide_resistance = resistance
        self.sunlight = sunlight
        Identifiable.__init__(self)