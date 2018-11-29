import abc
#
# Meat class + Meat Ingredients
#
class Meat:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __str__(self): pass

class Pepperoni(Meat):
    def __str__(self):
        return "Pepperoni"

class Sausage(Meat):
	def __str__(self):
		return "Sausage"

class Bacon(Meat):
	def __str__(self):
		return "Bacon"

class GroundBeef(Meat):
	def __str__(self):
		return "Ground Beef"

class Chicken(Meat):
	def __str__(self):
		return "Chicken"

class Ham(Meat):
	def __str__(self):
		return "Ham"

class Anchovies(Meat):
	def __str__(self):
		return "Anchovies"