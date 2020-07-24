from misc import Identifiable

class Plant(Identifiable):

    def __init__(self, species, season, seeds,  resistance, sunlight):
        self.species = species
        self.peak_season = season
        self.seeds_produced = seeds
        self.insecticide_resistance = resistance
        self.sunlight = sunlight
        Identifiable.__init__(self)