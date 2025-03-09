class Carte:	
	def __init__(self, valeur, couleur):
		"""
		Initialise la classe carte
		Parameters
		----------
		valeur : str
		couleur : str
		"""
		if not str(valeur) in ("As","2","3","4","5","6","7","8","9","Valet","Dame","Roi") or not str(couleur) in ("Pique", "Carreau", "Coeur", "Trêfle"):
			raise ValueError()
		self.__valeur = valeur
		self.__couleur = couleur

	@property
	def valeur (self):
		"""renvoie la valeur de la carte
		Return
		------
		str
		>>> valeur(Carte("2","Carreau"))
		"2"
		"""
		return self.__valeur

	@property
	def couleur(self):
		return self.__couleur

	def __str__(self):
		return f"{self.__valeur} de {self.__couleur.lower()}"

	def __repr__(self):
		return f"Carte({self.__valeur}, {self.__couleur})"

	def __eq__ (self, other):
		return isinstance(other, Carte) and self.repr == other.repr

	def __hash__ (self):
		pass