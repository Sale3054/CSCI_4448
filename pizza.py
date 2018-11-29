from flask import * 
from IngredientFactory import * 
from Pizza import *
from Meat import *
from Veggie import *
from Cheese import * 
from Sauce import * 
from Dough import * 

import abc

class BoulderIngredientFactory(IngredientFactory):

	def create_dough(self):
		return ThickCrust()

	def create_sauce(self):
		return Mozzarella()

	def create_cheese(self):
		return MarinaraSauce()

	def create_veggies(self):
		return [BlackOlives(), Spinach(), BananaPeppers()]

	def create_meats(self):
		return Pepperoni()

class CheesePizza(Pizza):

	def __init__(self, ingredient_factory):
		super(CheesePizza, self).__init__()
		self.factory = ingredient_factory

	def prepare(self):
		print ("Preparing a " + self.name + ".")
		self.dough = self.factory.create_dough()
		self.sauce = self.factory.create_sauce()
		self.cheese = self.factory.create_cheese()

class PepperoniPizza(Pizza):

	def __init__(self, ingredient_factory):
		super(CheesePizza, self).__init__()
		self.factory = ingredient_factory

	def prepare(self):
		print ("Preparing a " + self.name + ".")
		self.dough = self.factory.create_dough()
		self.sauce = self.factory.create_sauce()
		self.cheese = self.factory.create_cheese()

class VeggiePizza(Pizza):

	def __init__(self, ingredient_factory):
		super(CheesePizza, self).__init__()
		self.factory = ingredient_factory

	def prepare(self):
		print ("Preparing a " + self.name + ".")
		self.dough = self.factory.create_dough()
		self.sauce = self.factory.create_sauce()
		self.cheese = self.factory.create_cheese()


#
# Pizza Stores
#

class PizzaStore:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def create_pizza(self, item): pass

	def order_pizza(self, pizza_type):
		pizza = self.create_pizza(pizza_type)
		print(" === Making a " + pizza.name + " === \n")

		pizza.prepare()
		pizza.bake()
		pizza.cut()
		pizza.box()
		print("Total Price: $" + str(pizza.calculate_price()))

		return pizza

class BoulderPizzaStore(PizzaStore):

	def create_pizza(self, item):
		pizza = None
		ingredient_factory = BoulderIngredientFactory()

		if item == "cheese":
			pizza = CheesePizza(ingredient_factory)
			pizza.name = "Boulder Style Cheese Pizza"

		return pizza

class DIYPizza(Pizza):
	def __init__(self, ingredient_factory):
		super(DIYPizza, self).__init__()
		self.factory = ingredient_factory

	def prepare(self, dough = "", sauce = "", cheese = "", veggies = [], meats = []):
		print ("Preparing a " + self.name + ".")
		self.dough = dough
		self.sauce = sauce
		self.cheese = cheese
		self.veggies = veggies
		self.meats = meats



app = Flask(__name__)

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/', methods=['POST'])
def main_post():
	patron_name = request.form.get('name')
	pizza_selection = request.form.get('topping')
	sauce_selection = request.form.get('sauce')
	Boulder = BoulderPizzaStore()
	pizza = Boulder.order_pizza(pizza_selection)
	print("Some dude ordered a " + str(pizza) + "\n")
	
	text_message = patron_name + " has ordered a " + str(pizza)
	return render_template('main.html', message=text_message)

if __name__ == '__main__':
	app.run()
