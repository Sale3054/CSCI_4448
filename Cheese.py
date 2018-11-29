import abc
#
# Cheese class + Cheese Ingredients
#
class Cheese:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __str__(self): pass

class CreamCheese(Cheese):
	def __init__(self):
		self.price = 0.5
		
	def __str__(self):
		return "Cream Cheese"

class VeganCheese(Cheese):
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Vegan Cheese"

class Mozzarella(Cheese):
	def __init__(self):
		self.price = 0.5

	def __str__(self):
		return "Mozzarella Cheese"

class Parmesan(Cheese):
	def __init__(self):
		self.price = 0.5

	def __str__(self):
		return "Parmesan Cheese"

class Feta(Cheese):
	def __init__(self):
		self.price = 0.5

	def __str__(self):
		return "Feta Cheese"
		
class Ricotta(Cheese):
	def __init__(self):
		self.price = 0.5

	def __str__(self):
		return "Ricotta Cheese"
