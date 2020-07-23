from .. import Plant
from .. import Habitats

class Blue_Jade(Plant):
    def __init__(self, season, seeds, habitats = ["Grassland", "Swamp"], species = "Blue Jade",   ):
        Plant.__init__(self, species, season, seeds)
