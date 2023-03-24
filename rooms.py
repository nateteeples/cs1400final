class Room():
	def __init__(self):
		self.items = []
		self.usable = {}
		self.movements = []
		self.descriptions = {}
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