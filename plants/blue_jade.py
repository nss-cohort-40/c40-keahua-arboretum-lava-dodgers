from .plant import Plant
from .properties import Requires_Rainfall
from .properties import Requires_Current
from .properties import Requires_Freshwater

class Blue_Jade(Plant, Requires_Rainfall, Requires_Current, Requires_Freshwater):
    def __init__(self):
        Plant.__init__(self, "Blue Jade", "Spring", 0, "Medium", "Partial")
        Requires_Rainfall.__init__(self, False)
        Requires_Current.__init__(self, False)
        Requires_Freshwater.__init__(self, True)
