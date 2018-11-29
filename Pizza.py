#
# Base Pizza construction
#
import abc

class Pizza:
	#metaclass for @abstractmethod
	__metaclass__ = abc.ABCMeta

	def __init__(self, name = None, dough = None, sauce = None, 
		veggies = [], cheese = None, meats = []):
		self.name = name
		self.dough = dough
		self.sauce = sauce
		self.veggies = veggies
		self.cheese = cheese
		self.meats = meats

	@abc.abstractmethod
	def prepare(self): pass

	def bake(self): print (f"Cooking your {self.name}! Just 25 more minutes!")
	def cut(self): print (f'A professional is cutting the {self.name} now!')
	def box(self): print ("We're placing your {self.name} in a secure transportation mechanism!")
	def __str__(self):
		final_list = [self.dough, self.sauce, self.cheese] + self.veggies + self.meats
		final_pizza = self.name + ', which consists of: \n'
		for i in final_list:
			final_pizza += str(i)
			if i != final_list[-1]: 
				final_pizza += ", "
			else:
				final_pizza += '.\n'

		return final_pizza