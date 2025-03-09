from carte import Carte
import copy


class Combinaison:
    """caca"""

    def __init__(self, cartes):
        if not isinstance(cartes, tuple) or not all(
            isinstance(i, Carte) for i in cartes
        ):
            raise TypeError()
        self.__cartes = cartes

    @property
    def extraction(self):
        return copy.deepcopy(self.__cartes)

    def __eq__(self, other):
        if self.extraction == () and other.extraction == ():
            return True
        elif isinstance(self, Combinaison) and isinstance(other, Combinaison):
            if set(self) == set(other): 
                return True
            return False
        return False

    def __str__(self):
        k = self.extraction
        z = {str(i) for i in k[:-1]}
        return f"({', '.join(z)}, {str(k[-1])})"

    def __len__(self):
        return len(self.extraction)

    def est_brelan(self):
        pass
