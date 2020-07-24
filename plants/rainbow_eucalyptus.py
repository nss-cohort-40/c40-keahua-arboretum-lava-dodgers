from .plant import Plant
from .properties import Requires_Rainfall


class Rainbow_Eucalyptus(Plant):
    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "All", 8, "Low", "Shade")
        Requires_Rainfall.__init__(self, True)
