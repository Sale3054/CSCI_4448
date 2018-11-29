import abc
#
# Veggie Class + Veggie Ingredients
#
class Veggie:
	"""
	overaching Veggie ingredient class, of which specific Veggie ingredients can inherit and modify from.
	"""
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __str__(self): pass


class GreenPeppers(Veggie):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Green Peppers"

class GreenOlives(Veggie):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Green Olives"

class BananaPeppers(Veggie):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Banana Peppers"

class ArtichokePeppers(Veggie):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Artichoke Peppers"

class Garlic(Veggie):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Garlic"

class JalapenoPeppers(Veggie):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Jalapenos"

class Mushroom(Veggie):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Mushrooms"

class Spinach(Veggie):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Spinach"

class SundriedTomatoes(Veggie):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Sundried Tomatoes"

class Basil(Veggie):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Basil"

class Pineapple(Veggie):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Pineapple"

class BlackOlives(Veggie):
	"""
	instantiate price point of ingredient and create a new ToString() representation 
	"""
	def __init__(self):
		self.price = 0.5
	def __str__(self):
		return "Black Olives"