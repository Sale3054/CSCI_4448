#
# Ingredients and their construction
#

import abc

class IngredientFactory:
	#Need this so we can apply abstract method decorator
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def create_dough(self): pass

	@abc.abstractmethod
	def create_sauce(self): pass
	
	@abc.abstractmethod
	def create_cheese(self): pass
	
	@abc.abstractmethod
	def create_veggies(self): pass
	
	@abc.abstractmethod
	def create_meats(self): pass
