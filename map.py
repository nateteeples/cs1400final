floor0map = [["\n ", " ", " ", "┌", "−", "┐", " ", " ", " ", " ", " ", " ", " ", " ", " ", "   Ground Level"], 
[" ", " ", " ", "│", "O", "│", " ", " ", " ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", "│", " ", "│", " ", " ", " ", " ", " ", " ", " ", " ", " ", "   - Key -"],
["┌", "−", "−", "┘", " ", "│", " ", " ", " ", " ", " ", " ", " ", " ", " ", "   □: Wall"],
["│", "O", " ", " ", "O", "│", " ", " ", " ", " ", " ", " ", " ", " ", " ", "   O: Room"],
["└", "−", "−", "┐", " ", "│", " ", " ", " ", " ", " ", " ", " ", " ", " ", "   =: Door"],
[" ", " ", " ", "│", " ", "│", " ", " ", " ", " ", " ", " ", " ", " ", " ", "   ↕: Staircase"],
[" ", " ", " ", "│", "O", "│", " ", " ", " ", " ", " ", " ", " ", " ", " ", "   X: You are here"],
[" ", " ", " ", "│", " ", "│", " ", " ", " ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", "│", " ", "└", "−", "−", "−", "−", "−", "−", "−", "−", "┐"],
[" ", " ", " ", "│", "O", " ", " ", "↓", " ", " ", "O", " ", " ", "↑", "│"],
[" ", " ", " ", "└", "−", "−", "┐", " ", "┌", "┐", " ", "┌", "┐", " ", "│"],
[" ", " ", " ", " ", " ", " ", "│", " ", "│", "│", " ", "│", "│", "=", "│"],
[" ", " ", " ", " ", " ", " ", "│", "O", "│", "│", "O", "│", "│", "O", "│"],
[" ", " ", " ", " ", " ", " ", "└", "=", "┘", "└", "−", "┘", "└", "−", "┘"],
[" ", " ", " ", " ", " ", " ", "│", " ", "│", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", "│", "O", "│", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", "└", "−", "┘", " ", " ", " ", " ", " ", " \n"]]
for line in floor0map:
	linetext = ""
	for char in line:
		linetext += char
	print(linetext)