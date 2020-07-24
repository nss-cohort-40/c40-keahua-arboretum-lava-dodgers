from .plant import Plant
from .properties import Requires_Elevation

class Mountain_Apple(Plant):
    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree", "All", 17, "High", "Partial")
        Requires_Elevation.__init__(self, True)