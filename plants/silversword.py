from .plant import Plant


class Silversword(Plant):
    def __init__(self):
        Plant.__init__(self, "Silversword", "Fall", 22, ["Grasssland"], "High", "Full")
