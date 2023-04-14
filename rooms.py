from numpy import array

MOVEMENTS = {'north': array([0, 1, 0]), 'south': array([0, -1, 0]), 'east': array([-1, 0, 0]), 'west': array([1, 0, 0]), 'up': array([0, 0, 1]), 'down': array([0, 0, -1])}

class Room():
	def __init__(self):
		self.items = []
		self.usable = {}
		self.movements = []
		self.descriptions = {}
	def move(self, player):
		print(f"You can move in one of the following directions:\n{self.movements}")
		player_movement = input(f"Input a movement: ")
		if player_movement in MOVEMENTS:
			if player_movement in self.movements:
				print(f"Moving {player_movement}")
				player.set_move(player_movement)
			else:
				print(f"You can't move {player_movement} in this room")
		else:
			print(f"'{player_movement}' is not a valid input.\nValid inputs include north, south, east, west, up, or down")
	def get(self, player):
		if self.items:
			item = input("What item would you like to pick up?\n").lower()
			if item in self.items:
				self.items.remove(item.lower())
				player.inv.append(item.lower())
				print(f"{item.title()} has been added to your inventory")
			else:
				print(f"There is no {item} in this room")
		else:
			print("There are no items in this room")
	def use(self, player):
		if player.inv:
			print(f"{player.name}'s Inventory:")
			for item in player.inv:
				print(f"{item}")
			selection = input("What item would you like to use?\n").lower()
			if selection in player.inv:
				if selection in self.usable:
					print(self.usable[selection])
					player.inv.remove(selection)
					del self.usable[selection]
					self.action(selection)
				else:
					print(f"You can't use '{selection}' here.")
			else:
				print(f"'{selection}' was not found in your inventory.")
		else:
			print("Your inventory is empty, no items to use.")
	def desc(self):
		get = tuple(self.items), tuple(self.usable)
		return "\n\n"+self.descriptions.get(get, "Error - Room description not found")
	def action(self, item):
		#check item type and do corresponding action
		if item == 'key':
			self.movements.append('north')
		pass

rooms = {}
r = Room()
r.items.append('sword')
r.items.append('key')
r.usable['key'] = "You can use the key to unlock the large door"
r.descriptions[(('sword', 'key'), ('key',))] = "You enter a room with a large door and a keyhole. On the ground lies a sword and a key."
r.descriptions[(('sword',), ())] = "You open the door using the key. You can now move north. On the groud lies a sword."
r.descriptions[((), ())] = "You open the door using the key. You can now move north."
r.movements.append('up')
rooms[(0, 0, 0)] = r

r = Room()
r.items.append("test1")
r.movements.append('south')
rooms[(0, 1, 0)] = r

r = Room()
r.items.append("test2")
r.movements.append('down')
rooms[(0, 0, 1)] = r