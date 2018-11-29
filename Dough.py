
import abc

#
# Dough Class + Dough Ingredients
#

class Dough: 
	"""
	overaching ingredient class, of which specific ingredients can inherit and modify from.
	"""
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __str__(self): pass

class GlutenFree(Dough):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Gluten Free Crust"

class ThickCrust(Dough):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Thick Crust"

class ThinCrust(Dough):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Thin Crust"

class CheeseyCrust(Dough):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Cheesey Crust"        