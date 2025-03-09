from carte import Carte
class Combinaison:
	def __init__ (self, cartes):
		if not isinstance(cartes,tuple) or not (isinstance(i,Carte) for i in cartes):
			raise TypeError()
		self.__cartes = cartes

	@property
	def extraction (self):
		return copy.deepcopy(self.__cartes)

	def __eq__ (self, other):
		if self.extraction(), other.extraction() == (),()
			return True
		elif isinstance(self,Combinaison) and isinstance(other,Combinaison):
			if set(self) == set(other):                ###### Attention icic pas s\'fbr de comment r\'e9agi "set()"
				return True
			return False

	def __str__(self):
		k=extraction(self)
		return f"({str(i) for i in k[:-1]}, str(k[len(k)]))"

	def __len__ (self):
		return len(extraction(self))

	def est_brelan (self):
		pass