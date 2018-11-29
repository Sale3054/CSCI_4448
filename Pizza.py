#
# Base Pizza construction
#
import abc

class Pizza:
	# metaclass for @abstractmethod
	__metaclass__ = abc.ABCMeta

	def __init__(self, name = None, dough = None, sauce = None, 
		veggies = [], cheese = None, meats = [], price = 5):
		self.name = name
		self.dough = dough
		self.sauce = sauce
		self.veggies = veggies
		self.cheese = cheese
		self.meats = meats
		self.price = price

	@abc.abstractmethod
	def prepare(self): pass


	def calculate_price(self):
		total_price = self.price
		attr_list = [self.dough, self.sauce, self.cheese]
		attr_list= attr_list + self.meats
		attr_list = attr_list + self.veggies


		'''

		This code is currently broken...yay

		vars() returns a dictionary of key/value pairs of the
		name of the attribute and its value. So, we strip off the keys, leaving only
		the values(). Then, we case the Dictionary (that has empty key values) into
		a list, so that we can remove the items from the list that do not
		have a price attribute- e.g. any of the attributes that are not 
		ingredients.
		'''


		'''
		total_price = 0
		print("\nBEGIN ATTR \n")
		attr_list = list(vars(self).values())
		print(attr_list)
		for i in attr_list:
			#check if it's an ingredient (e.g. it has a price)
			if not hasattr(i, 'price') or i == None or i == []:
				attr_list.remove(i)
			#check if this is a list, if so, concatenate to the
			#overaching list, so we don't have to worry about indexing
			if type(i) == list:
				temp_list = i
				attr_list.remove(temp_list)
				attr_list += temp_list
		print("Filtered List: \n")

		print(attr_list)
		for i in attr_list:
			total_price += i.price
			print(i)
		'''
		for i in attr_list:
			if i.price is not None:
				total_price = total_price + i.price
		return total_price


	def bake(self): print("Cooking your {}! Just 25 more minutes!".format(self.name))
	def cut(self): print('A professional is cutting the {} now!'.format(self.name))
	def box(self): print("We're placing your {} in a secure transportation mechanism!".format(self.name))

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


