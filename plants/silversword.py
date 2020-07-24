from .plant import Plant
from .properties import Requires_Rainfall


class Silversword(Plant):
    def __init__(self):
        Plant.__init__(self, "Silversword", "Fall", 22, "High", "Full")
        Requires_Rainfall.__init__(self, False)
