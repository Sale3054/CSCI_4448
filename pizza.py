from flask import * 
from IngredientFactory import * 
from Pizza import *
from Meat import *
from Veggie import *
from Cheese import * 
from Sauce import * 
from Dough import * 

import sqlite3
import abc



class BoulderIngredientFactory(IngredientFactory):
	"""
	BoulderIngredientFactory encapsulates various ingredients appropriate to the mentioned Locale, in this case, Boulder.
	"""

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
	"""
	CheesePizza is a concrete instance of Pizza; an object to be created at the final stage when a Customer orders.
	"""

	def __init__(self, ingredient_factory):
		"""
		Construct a new CheesePizza object.

		:param factory: The name of the ingredient factory being used
		:return: returns nothing at all
		"""
		super(CheesePizza, self).__init__()
		self.factory = ingredient_factory

	def prepare(self):
		"""
		Override the abstract class declared in Pizza, and instantiate all appropriate ingredient values for the Pizza,
		(In the case of Cheese pizza, we only need Dough, Sauce and Cheese, as a Cheese pizza is very plain otherwise)
		
		:param dough: Calls create_dough() constructor of the factory used
		:param sauce: Calls create_sauce() constructor of the factory used
		:param cheese: Calls create_cheese() constructor of the factory used
		:return: returns nothing at all
		"""
		print ("Preparing a " + self.name + ".")
		self.dough = self.factory.create_dough()
		self.sauce = self.factory.create_sauce()
		self.cheese = self.factory.create_cheese()

class PepperoniPizza(Pizza):
	"""
	A concrete instance of Pizza; an object to be created at the final stage when a Customer orders.
	"""

	def __init__(self, ingredient_factory):
		"""
		Construct a new PepperoniPizza object.

		:param factory: The name of the ingredient factory being used
		:return: returns nothing at all
		"""
		super(CheesePizza, self).__init__()
		self.factory = ingredient_factory

	def prepare(self):
		"""
		Override the abstract class declared in Pizza, and instantiate all appropriate ingredient values for the Pizza,
		(In the case of Pepperoni pizza, we only need Dough, Sauce, Cheese and Pepperoni)
		
		:param dough: Calls create_dough() constructor of the factory used
		:param sauce: Calls create_sauce() constructor of the factory used
		:param cheese: Calls create_cheese() constructor of the factory used
		:param meats: Calls create_meats() constructor of the factory used
		:return: returns nothing at all
		"""
		print ("Preparing a " + self.name + ".")
		self.dough = self.factory.create_dough()
		self.sauce = self.factory.create_sauce()
		self.cheese = self.factory.create_cheese()
		self.meats = self.factory.create_meats()

class VeggiePizza(Pizza):
	"""
	A concrete instance of Pizza; an object to be created at the final stage when a Customer orders.
	"""
	def __init__(self, ingredient_factory):
		"""
		Construct a new VeggiePizza object.

		:param factory: The name of the ingredient factory being used
		:return: returns nothing at all
		"""
		super(CheesePizza, self).__init__()
		self.factory = ingredient_factory

	def prepare(self):
		"""
		Override the abstract class declared in Pizza, and 
		instantiate all appropriate ingredient values for the Pizza,
		
		:param dough: Calls create_dough() constructor of the factory used
		:param sauce: Calls create_sauce() constructor of the factory used
		:param cheese: Calls create_cheese() constructor of the factory used
		:return: returns nothing at all
		"""
		print ("Preparing a " + self.name + ".")
		self.dough = self.factory.create_dough()
		self.sauce = self.factory.create_sauce()
		self.cheese = self.factory.create_cheese()


#
# Pizza Stores
#

class PizzaStore:
	""" Abstract class to support factory design pattern- PizzaStore supports localization of franchise stores"""
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def create_pizza(self, item): pass

	def order_pizza(self, pizza_type):
		""" place an order for whatever pizza is passed in, based on the locale provided"""
		pizza = self.create_pizza(pizza_type)
		print(" === Making a " + pizza.name + " === \n")

		pizza.prepare()
		pizza.bake()
		pizza.cut()
		pizza.box()
		print("Total Price: $" + str(pizza.calculate_price()))

		return pizza

class BoulderPizzaStore(PizzaStore):
	""" subclass of the PizzaStore class, Boulder Localization specific implementation of the pizza store"""

	def create_pizza(self, item):
		""" creates a new pizza object
		:param pizza: pizza object to be returned, containing the list of  ingredients and summed price
		:param ingredient_factory: factory from which our ingredients will be sourced (and our constructors)
		:return: pizza object

		"""
		pizza = None
		ingredient_factory = BoulderIngredientFactory()

		if item == "cheese":
			pizza = CheesePizza(ingredient_factory)
			pizza.name = "Boulder Style Cheese Pizza"

		return pizza

class DIYPizza(Pizza):
	""" A DIY pizza pattern. Currently questioning pulling this from the code as I am unsure how to fit this 
	into the present design pattern.
	"""
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
	"""
	main function that creates the databases of the webapp and directs the user to the main page.
	Database is cleared and recreated each time the program is ran, for the sake of demo/testing purposes.
	In a production environment this would need to change.
	"""
	conn = sqlite3.connect('database.db')
	print("Opened database successfully")

	conn.execute('DROP TABLE IF EXISTS customers')
	conn.execute('CREATE TABLE customers (patron_name TEXT, addr TEXT, pizza_ TEXT)')

	print("Table created successfully")
	conn.close()

	return render_template('main.html')

@app.route('/', methods=['POST'])
def main_post():
	"""
	Handles the user request after the form is submitted, creating a database entry.
	msg displays the result of the attempt to create the database.
	 If unsuccessful, will inform the user with msg that it was so, likewise if it is successful.

	:param patron_name: name of the customer creating the request
	:param pizza_selection: the type of pizza of which needs to be created
	:param Boulder: Franchise locale in which this implementation is based (factory)
	:param pizza: the pizza object
	:param addr: address of the patron for delivery purposes
	:param text_message: placeholder text in the case that msg is not properly assigned
	:param msg: status text of the database- whether or not the entry was successfully created
	:param pizza_: the ToString() (__str__) representation of the pizza object
	:return: render template-> renders the subsequent page following the form submittal, displaying the database
	post entry
	"""
	patron_name = request.form.get('name')
	pizza_selection = request.form.get('topping')
	sauce_selection = request.form.get('sauce')
	Boulder = BoulderPizzaStore()
	pizza = Boulder.order_pizza(pizza_selection)
	print(patron_name + " ordered a " + str(pizza) + "\n")

	addr = "standard street address filler"
	text_message = patron_name + " has ordered a " + str(pizza)
	msg = text_message
	pizza_ = str(pizza)

	try:
		with sqlite3.connect('database.db') as con:
			cur = con.cursor()
			cur.execute("INSERT INTO customers (patron_name, addr, pizza_) VALUES (?, ?, ?)", (patron_name, addr, pizza_) )
			con.commit()
			print("DB: Record Successfully added")
			msg = patron_name + "'s order for a " + pizza_ + " was successfully added."

	except:
		con.rollback()
		print("DB: There was an error.")
		msg = "error in inserting the operation"
	finally:
		return render_template('result.html', msg = msg)
	con.close()


@app.route('/tablehs')
def list_db_tables():
	"""
	list the database tables after redirecting to the "tablehs" page
	"""
	con = sqlite3.connect("database.db")
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute("select * from customers")
	rows = cur.fetchall(); 
	return render_template("tablehs.html", rows = rows)

if __name__ == '__main__':
	app.run()
