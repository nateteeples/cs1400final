from numpy import array

MOVEMENTS = {'north': array([0, 1, 0]), 'south': array([0, -1, 0]), 'east': array([1, 0, 0]), 'west': array([-1, 0, 0]), 'up': array([0, 0, 1]), 'down': array([0, 0, -1])}

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
			self.movements.append('south')
		pass

rooms = {}
r = Room()
r.descriptions[((), ())] = "You enter a field with an abandoned house to the north."
r.movements.append('north')
rooms[(0, 0, 0)] = r

r = Room()
r.items.append("key")
r.descriptions[(('key',), ())] = "You enter the house, and the door slams behind you, appearing to be stuck. Inside is a large spiral staircase to the north, with branching rooms on each side of the staircase. A key lies on a table by the door."
r.descriptions[((), ())] = "You enter the house, and the door slams behind you, appearing to be stuck. Inside is a large spiral staircase to the north, with branching rooms on each side of the staircase."
r.movements.append('north')
rooms[(0, 1, 0)] = r

r = Room()
r.descriptions[((), ())] = "There are rooms on each side of the staircase. The staircase appears to lead to an upper floor."
r.movements.append('west')
r.movements.append('east')
r.movements.append('up')
rooms[(0, 2, 0)] = r

r = Room()
r.descriptions[((), ())] = "You walk into the dining room. There is a large table surrounded by broken chairs and shards of dishes scattered on the floor. To the north there is a kitchen."
r.movements.append('north')
r.movements.append('east')
rooms[(-1, 2, 0)] = r

r = Room()
r.descriptions[((), ())] = "You walk into the kitchen. Broken cabinets hang on the walls, and the flooring is covered in dust and dirt. To the north is a hallway."
r.movements.append('north')
r.movements.append('south')
rooms[(-1, 3, 0)] = r

r = Room()
r.descriptions[((), ())] = "The hall branches north and west, with a door at each end."
r.movements.append('north')
r.movements.append('south')
r.movements.append('west')
rooms[(-1, 4, 0)] = r

r = Room()
r.usable['safe-code'] = "You key in the safe code on the safe."
r.descriptions[((), ('safe-code'))] = "You enter the master bedroom. There is a large, empty mattress in the center of the room. On a bedside table lies a safe."
r.descriptions[((), ())] = "The safe clicks open. Inside is a knife."
r.movements.append('east')
rooms[(-2, 4, 0)] = r

r = Room()
r.descriptions[((), ())] = "You enter an empty bedroom."
r.movements.append('south')
rooms[(-1, 5, 0)] = r

r = Room()
r.descriptions[((), ())] = "You enter the living room. Trash clutters the floor, with a well worn couch in the center of the room. There is a hallway to the east."
r.movements.append('east')
r.movements.append('west')
r.movements.append('south')
rooms[(1, 2, 0)] = r

r = Room()
r.descriptions[((), ())] = "You enter a dirty bathroom."
r.movements.append('north')
rooms[(1, 1, 0)] = r

r = Room()
r.items.append('book')
r.descriptions[(('book',), ())] = "You enter a bedroom. The room appears well kept, with a single book lying on a bed."
r.descriptions[((), ())] = "You enter a bedroom. The room appears well kept, with a clean bed against the wall."
r.movements.append('north')
rooms[(1, 1, 0)] = r

r = Room()
r.usable['key'] = "You use the key to unlock the door."
r.descriptions[((), ('key',))] = "In the hall is a staircase and a locked door."
r.descriptions[((), ())] = "In the hall is a staircase and an open door to the south."
r.movements.append('east')
r.movements.append('up')
rooms[(2, 2, 0)] = r

#template rooms
r = Room()
r.items.append("sword")
r.usable['key'] = "You can use the key to unlock the large door"
r.descriptions[(('sword',), ('key',))] = "You enter a room with a sword on the ground and a large door with a keyhole."
r.descriptions[(('sword'), ())] = "You open the door using the key. You can now move north. A sword lies on the ground."
r.descriptions[((), ('key',))] = "You enter a room with a large door and a keyhole."
r.descriptions[((), ())] = "You open the door using the key. You can now move north."
r.movements.append('south')
rooms[(0, 1, 10)] = r

r = Room()
r.items.append("test2")
r.movements.append('down')
rooms[(0, 0, 11)] = r

r = Room()
r.items.append("test3")
r.movements.append('south')
rooms[(0, 2, 10)] = r