import abc
#
# Sauce class + Sauce Ingredients
#
class Sauce:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __str__(self): pass

class MarinaraSauce(Sauce):
	def __str__(self):
		return "Marinara Sauce"

class WhiteSauce(Sauce):
	def __str__(self):
		return "White Sauce"

class BBQSauce(Sauce):
	def __str__(self):
		return "BBQ Sauce"
