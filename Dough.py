
import abc

#
# Dough Class + Dough Ingredients
#

class Dough: 
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __str__(self): pass

class GlutenFree(Dough):
	def __str__(self):
		return "Gluten Free Crust"

class ThickCrust(Dough):
	def __str__(self):
		return "Thick Crust"

class ThinCrust(Dough):
	def __str__(self):
		return "Thin Crust"

class CheeseyCrust(Dough):
	def __str__(self):
		return "Cheesey Crust"        