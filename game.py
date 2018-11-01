"""
game.py

Turn based game written in Python for CSCI 4448.
@author Samuel Leon
"""
import random

class Game:
	def create_item(item):
		new_item = Item()

	def create_NPC(name, type = None):
		monster = Character.NPC(name)
		return monster

	def new_room():
		new_room = Room()
		new_room.contains.append(Game.create_NPC("Spooky Scary Skeleton"))
		new_room.contains.append(Game.create_item("Potion"))
		return new_room

class Item:
	def __init__(self):
		self.name = ""
		self.rarity = "common"
	def common_potion(target, rarity = "common"):
		target.health += 25
	def uncommon_potion(target, rarity = "uncommon"):
		target.health += 50
	def rare_potion(target, rarity = "rare"):
		target.health += 75
	def epic_potion(target, rarity = "epic"):
		target.health += 100

class Character:
	class Player:
		def __init__(self, name):
			self.location = Room()
			self.name = name
			self.class_type = "Warrior"
			self.health = 100
			self.mana = 50
			self.attack_value = 10

		"""
		Function Move:
		Move the character from one room to another.
		@param direction: direction will be the direction that the character moves.
		"""
		def move(self, direction):
			self.location = getattr(self.location, direction)

		def basic_attack(self, target):
			print(f"Rolling to attack the {target.name}.")
			roll = random.randint(0, 100)
			print("You rolled a {roll}.")
			if roll > 50:
				target.health = target.health - self.attack_value
				print(f"You hit {target.name} for {self.attack_value}. {target.name}\'s health is now {target.health}.")
			else:
				print("You missed!")

		"""
		Function pickup:
		will place the item in the user's inventory.
		"""
		def pickup():
			if any(isinstance(x, Item) for x in self.location.contains):
				self.inventory.append(x)
				self.location.contains.pop(x)

	class NPC:
		def __init__(self, name):
			self.name = name
			self.attack_value = random.randint(0, 10)
			self.health = 100
class Room:
	"""
	Each room should have the chance to contain an enemy and an item.
	"""
	def __init__(self):
		self.north = None
		self.south = None
		self.east = None
		self.west = None
		self.contains = []

	def setNorth(new_val):
		self.north = new_val
	def setSouth(new_val):
		self.north = new_val
	def setEast(new_val):
		self.east = new_val
	def setWest(new_val):
		self.west = new_val

	def getNorth(new_val):
		return self.north
	def getSouth(new_val):
		return self.south
	def getWest(new_val):
		return self.west
	def getEast(new_val):
		return self.east

	
def main():
	mc_name = input("What is your character's name?")
	mc = Character.Player(mc_name)
	in_combat = False
	print("You have found yourself in a dungeon...")
	while(True):
		if any(isinstance(x, Character.NPC) for x in mc.location.contains):
			in_combat = True
		if in_combat:
			NPC = mc.location.contains[0]
			print(NPC)
			print(f"You have encountered a {NPC.name}!")
			selection = input("""What will you do?\n1.Attack\n2.Hide\n3.Quit\n""")
			
			if selection == '1':
				NPC.health = NPC.health - mc.attack_value
			elif selection == '2':
				roll = random.randint(1, 100)
				print("You try to hide yourself from the beast.")
				print(f"You rolled a {roll}.")
			elif selection == 3:
				return False

		selection = input("""\n1.Move North\n2.Move South\n3.Move East\n4.Move West\n""")
		if selection == '1':
			north_room = Game.new_room()
			mc.location.north = north_room
			north_room.south = mc.location
			mc.move('north')
		elif selection == '2':
			south_room = Game.new_room()
			mc.location.south = south_room
			south_room.north = mc.location
			mc.move('south')
		elif selection == '3':
			east_room = Game.new_room()
			mc.locationeast = east_room
			east_room.west = mc.location
			mc.move('east')
		elif selection == '4':
			west_room = Game.new_room()
			mc.location.west(west_room)
			west_room.east(mc.location)
			mc.move('west')

if __name__ == '__main__':
    main()