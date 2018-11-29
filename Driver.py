'''
Pizza Parlor

Author: Samuel Leon
Date: Fall 2018

'''
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

		return pizza

class BoulderPizzaStore(PizzaStore):

    def create_pizza(self, item):
        pizza = None
        ingredient_factory = BoulderIngredientFactory()

        if item == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "Boulder Style Cheese Pizza"
        return pizza



if __name__ == '__main__':
    nyStore = BoulderPizzaStore()
    pizza = nyStore.order_pizza("cheese")
    print("Some dude ordered a " + str(pizza) + "\n")

	