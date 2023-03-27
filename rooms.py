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

rooms = {}
r = Room()
r.items["test"]
r.movements['north', 'up']
rooms[(0, 0, 0)] = r

rooms = {}
r = Room()
r.items["test1"]
r.movements['south']
rooms[(0, 1, 0)] = r

rooms = {}
r = Room()
r.items["test2"]
r.movements['down']
rooms[(0, 0, 1)] = r