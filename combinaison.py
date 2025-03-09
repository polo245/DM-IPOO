{\rtf1\ansi\ansicpg1252\cocoartf2707
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww14920\viewh15000\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Combinaison:\
\
	def __init__ (self, cartes):\
		if not isinstance(cartes,tuple) or not (isinstance(i,Carte) for i in cartes):\
			raise TypeError()\
		self.__cartes = cartes\
	\
	@property\
	def extraction (self):\
		return copy.deepcopy(self.__cartes)\
		\
	def __eq__ (self, other):\
		if extraction(self),extraction(other) == (),()\
			return True\
		elif isinstance(self,Combinaison) and isinstance(other,Combinaison):\
			if set(self) == set(other):                ###### Attention icic pas s\'fbr de comment r\'e9agi "set()"\
				return True\
		return False\
	\
	def __str__(self):\
		k=extraction(self)\
		return f"(\{str(i)f", " for i in k[:-1]\}, str(k[len(k)]))"\
\
	def __len__ (self):\
		return len(extraction(self))\
\
	def est_brelan (self):\
		\
}