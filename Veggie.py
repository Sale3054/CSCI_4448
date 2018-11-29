import abc
#
# Veggie Class + Veggie Ingredients
#
class Veggie:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __str__(self): pass


class GreenPeppers(Veggie):
	def __str__(self):
		return "Green Peppers"

class GreenOlives(Veggie):
	def __str__(self):
		return "Green Olives"

class BananaPeppers(Veggie):
	def __str__(self):
		return "Banana Peppers"

class ArtichokePeppers(Veggie):
	def __str__(self):
		return "Artichoke Peppers"

class Garlic(Veggie):
	def __str__(self):
		return "Garlic"

class JalapenoPeppers(Veggie):
	def __str__(self):
		return "Jalapenos"

class Mushroom(Veggie):
	def __str__(self):
		return "Mushrooms"

class Spinach(Veggie):
	def __str__(self):
		return "Spinach"

class SundriedTomatoes(Veggie):
	def __str__(self):
		return "Sundried Tomatoes"

class Basil(Veggie):
	def __str__(self):
		return "Basil"

class Pineapple(Veggie):
	def __str__(self):
		return "Pineapple"

class BlackOlives(Veggie):
	def __str__(self):
		return "Black Olives"