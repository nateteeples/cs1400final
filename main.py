import pickle
import map
from numpy import array
from rooms import rooms, MOVEMENTS

VALID_ACTIONS = ('save', 'load', 'move', 'get', 'use', 'quit', 's', 'l', 'm', 'g', 'u', 'q')
restart = False

class Player():
	def __init__(self):
		self.pos = (0, 0, 0)
		self.inv = []
	def set_move(self, movement):
		self.pos = tuple(array(self.pos)+MOVEMENTS.get(movement,array([0,0,0])))
	def get_input(self):
		choice = input("┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐\n│ Input one of the following commands:   │\n│ move, get, use, save, load, help, quit │\n└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘\n\n").lower()
		while choice not in VALID_ACTIONS:
			print(f"\n\n'{choice}' is not a valid command")
			choice = input("┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐\n│ Input one of the following commands:   │\n│ move, get, use, save, load, help, quit │\n└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘\n\n").lower()
		return choice

def save():
	with open("save.bin", "wb") as save:
		pickle.dump(player, save)
		pickle.dump(rooms, save)
		pickle.dump(player.pos, save)
		print("\nYour progress has been saved")

def load():
	global player
	global rooms
	try:
		with open("save.bin", "rb") as save:
			player = pickle.load(save)
			rooms = pickle.load(save)
			player.pos = pickle.load(save)
			print("\nProgress successfully loaded")
	except FileNotFoundError:
		print("\nA save file was not found")

def main(player):
	global restart
	cmd = None
	while cmd != 'quit' and cmd != 'q':
		(x, y, z) = player.pos
		current_room = rooms.get(player.pos)
		(row, index) = current_room.mposition
		tempmap = map.Map()
		tempmap.output_map(row, index, z)
		del tempmap
		print(current_room.desc())
		if current_room.win and current_room.win == True:
			print("\nYou Win! Thanks for Playing!")
			break
		cmd = player.get_input()
		if cmd == 'quit' or cmd == 'q':
			print('\nThanks for Playing!')
		elif cmd == 'move' or cmd == 'm':
			current_room.move(player)
		elif cmd == 'get' or cmd == 'g':
			current_room.get(player)
		elif cmd == 'use' or cmd == 'u':
			current_room.use(player)
		elif cmd == 'save' or cmd == 's':
			save()
		elif cmd == 'load' or cmd == 'l':
			restart = True
			break

def start():
	print(" .----------------.  .----------------.  .----------------. \n| .--------------. || .--------------. || .--------------. |\n| |  _________   | || |  ____  ____  | || |  _________   | |\n| | |  _   _  |  | || | |_   ||   _| | || | |_   ___  |  | |\n| | |_/ | | \_|  | || |   | |__| |   | || |   | |_  \_|  | |\n| |     | |      | || |   |  __  |   | || |   |  _|  _   | |\n| |    _| |_     | || |  _| |  | |_  | || |  _| |___/ |  | |\n| |   |_____|    | || | |____||____| | || | |_________|  | |\n| |              | || |              | || |              | |\n| '--------------' || '--------------' || '--------------' |\n '----------------'  '----------------'  '----------------' \n .----------------.  .----------------.  .----------------.  .----------------.  .----------------. \n| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |\n| |  ____  ____  | || |     ____     | || | _____  _____ | || |    _______   | || |  _________   | |\n| | |_   ||   _| | || |   .'    `.   | || ||_   _||_   _|| || |   /  ___  |  | || | |_   ___  |  | |\n| |   | |__| |   | || |  /  .--.  \  | || |  | |    | |  | || |  |  (__ \_|  | || |   | |_  \_|  | |\n| |   |  __  |   | || |  | |    | |  | || |  | '    ' |  | || |   '.___`-.   | || |   |  _|  _   | |\n| |  _| |  | |_  | || |  \  `--'  /  | || |   \ `--' /   | || |  |`\____) |  | || |  _| |___/ |  | |\n| | |____||____| | || |   `.____.'   | || |    `.__.'    | || |  |_______.'  | || | |_________|  | |\n| |              | || |              | || |              | || |              | || |              | |\n| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |\n '----------------'  '----------------'  '----------------'  '----------------'  '----------------' \n     By Nate Teeples")
	print(f"\n\n{'new/n - Start a new game':^100}\n\n{'load/l - Load a previous game':^100}\n\n{'quit/q - Quit the game':^100}")
	cmd = input("\n\nInput a command: ").lower()
	VALID_CHOICES = ('new', 'load', 'quit', 'n', 'l', 'q')
	while cmd not in VALID_CHOICES:
		cmd = input("Input a command: ").lower()
	if cmd == 'new' or cmd == 'n':
		input("\n\nThis game is best played in a fullscreen or tall window. Press enter to continue.")
		player = Player()
		main(player)
	elif cmd == 'load' or cmd == 'l':
		player = Player()
		load()
		restart = False
		main(player)

start()

if restart:
	load()
	restart = False
	main(player)