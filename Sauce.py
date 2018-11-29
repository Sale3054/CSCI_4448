import abc
#
# Sauce class + Sauce Ingredients
#
class Sauce:
	"""
	overaching ingredient class, of which specific ingredients can inherit and modify from.
	"""
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __str__(self): pass

class MarinaraSauce(Sauce):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Marinara Sauce"

class WhiteSauce(Sauce):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "White Sauce"

class BBQSauce(Sauce):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "BBQ Sauce"
