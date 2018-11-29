
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

#
# Cheese class + Cheese Ingredients
#
class Cheese:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __str__(self): pass

class CreamCheese(Cheese):
	def __str__(self):
		return "Cream Cheese"

class VeganCheese(Cheese):
	def __str__(self):
		return "Vegan Cheese"

class Mozzarella(Cheese):
	def __str__(self):
		return "Mozzarella Cheese"

class Parmesan(Cheese):
	def __str__(self):
		return "Parmesan Cheese"

class Feta(Cheese):
	def __str__(self):
		return "Feta Cheese"
		
class Ricotta(Cheese):
	def __str__(self):
		return "Ricotta Cheese"
		
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