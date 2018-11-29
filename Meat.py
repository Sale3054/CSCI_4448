import abc
#
# Meat class + Meat Ingredients
#
class Meat:
	"""
	overaching ingredient class, of which specific ingredients can inherit and modify from.
	"""
	__metaclass__ = abc.ABCMeta
	@abc.abstractmethod

	def __str__(self): pass

class Pepperoni(Meat):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Pepperoni"

class Sausage(Meat):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Sausage"

class Bacon(Meat):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Bacon"

class GroundBeef(Meat):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Ground Beef"

class Chicken(Meat):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Chicken"

class Ham(Meat):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Ham"

class Anchovies(Meat):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Anchovies"