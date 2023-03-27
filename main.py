from numpy import array
from rooms import rooms, MOVEMENTS

VALID_ACTIONS = ('save', 'load', 'move', 'get', 'use', 'help')

class Player():
	def __init__(self):
		self.pos = (0, 0, 0)
		self.inv = []
		self.name = input("Input your name:\n").title()
	def set_move(self, movement):
		self.pos = tuple(array(self.pos)+MOVEMENTS.get(movement,array([0,0,0])))
	def get_input(self):
		choice = input("Input one of the following commands:\nmove, get, use, save, load, help").lower()
		while choice not in VALID_ACTIONS:
			print(f"'{choice}' is not a valid command")
			choice = input("Input one of the following commands:\nmove, get, use, save, load, help").lower()
		return choice

def main(player):
	cmd = None
	current_room = rooms.get(player.pos)
	while cmd != 'quit':
		#add room desc
		cmd = get_input()
		if cmd == 'quit':
			print('Thanks for Playing!')
		elif cmd == 'move':
			current_room.move(player)
		elif cmd == 'get':
			current_room.get(player)
		elif cmd == 'use':
			pass
		elif cmd == 'save':
			pass
		elif cmd == 'load':
			pass
		elif cmd == 'help':
			pass

main(Player())