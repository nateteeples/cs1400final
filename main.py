import pickle
import map
from numpy import array
from rooms import rooms, MOVEMENTS

VALID_ACTIONS = ('save', 'load', 'move', 'get', 'use', 'help', 'quit')
restart = False

class Player():
	def __init__(self):
		self.pos = (0, 0, 0)
		self.inv = []
		self.name = input("Input your name:\n").title()
	def set_move(self, movement):
		self.pos = tuple(array(self.pos)+MOVEMENTS.get(movement,array([0,0,0])))
	def get_input(self):
		choice = input("Input one of the following commands:\nmove, get, use, save, load, help, quit\n").lower()
		while choice not in VALID_ACTIONS:
			print(f"\n\n'{choice}' is not a valid command")
			choice = input("Input one of the following commands:\nmove, get, use, save, load, help, quit\n").lower()
		return choice

def save():
	with open("save.bin", "wb") as save:
		pickle.dump(player, save)
		pickle.dump(rooms, save)
		pickle.dump(player.pos, save)
		print("Your progress has been saved")

def load():
	global player
	global rooms
	try:
		with open("save.bin", "rb") as save:
			player = pickle.load(save)
			rooms = pickle.load(save)
			player.pos = pickle.load(save)
			print("Progress successfully loaded")
	except FileNotFoundError:
		print("A save file was not found")

player = Player()
def main(player):
	global restart
	cmd = None
	while cmd != 'quit':
		current_room = rooms.get(player.pos)
		(row, index) = current_room.mposition
		map.Map().output_map(row, index)
		print(current_room.desc())
		cmd = player.get_input()
		if cmd == 'quit':
			print('Thanks for Playing!')
		elif cmd == 'move':
			current_room.move(player)
		elif cmd == 'get':
			current_room.get(player)
		elif cmd == 'use':
			current_room.use(player)
		elif cmd == 'save':
			save()
		elif cmd == 'load':
			restart = True
			break
		elif cmd == 'help':
			#debug, change later
			print(player.pos)

main(player)

if restart:
	load()
	restart = False
	main(player)