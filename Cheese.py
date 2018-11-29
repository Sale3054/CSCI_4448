import abc
#
# Cheese class + Cheese Ingredients
#
class Cheese:
	"""
	overaching ingredient class, of which specific ingredients can inherit and modify from.
	"""
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __str__(self): pass

class CreamCheese(Cheese):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
		
	def __str__(self):
		return "Cream Cheese"

class VeganCheese(Cheese):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Vegan Cheese"

class Mozzarella(Cheese):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5

	def __str__(self):
		return "Mozzarella Cheese"

class Parmesan(Cheese):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5

	def __str__(self):
		return "Parmesan Cheese"

class Feta(Cheese):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5

	def __str__(self):
		return "Feta Cheese"
		
class Ricotta(Cheese):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5

	def __str__(self):
		return "Ricotta Cheese"
