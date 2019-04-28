
def main():
	print("1: button")
	print("2: 6 horizontal wires")
	print("3: 123abc wires")
	print("4: led star wires")
	print("5: symbols")
	puzzle = int(input("which puzzle do you have: "))

	if int(puzzle) == 1: button()
	elif int(puzzle) == 2: horizontal6wires()
	elif int(puzzle) == 3: abc123wires()
	elif int(puzzle) == 4: ledStarWires()
	elif int(puzzle) == 5: symbolsKeypads()
	else:
		print("invalid selection")
		main()


def button():
	color = str(input("which color is the button: ")).lower()
	text = str(input("what is the text on the button: ")).lower()
	batteries = int(input("how many batteries are there: "))


	if color == "blue" and text == "abort":
		HoldButton()

	elif (batteries > 1 and text == "detonate"): 
		print("press and immediately release")

	elif color == "white":
		CARlabel = str(input("is there a lit indicator with a CAR label: ")).lower()
		if CARlabel == "y":
			HoldButton()
		else:
			HoldButton()

	elif batteries > 2:
		FRKlabel = str(input("is there a lit indicator with a FRK label: ")).lower()
		if FRKlabel == "y":
			print("press and immediately release")
		else:
			HoldButton()

	elif color == "red" and text == "hold":
		print("press and immediately release")

	else:
		HoldButton()


def HoldButton():
	print("------------PRESS AND HOLD THE BUTTON-----------------")
	color = str(input("which color is the strip: ")).lower()
	if color == "blue": print("release with a 4 in any position")
	elif color == "yellow":print("release with a 5 in any position")
	else:print("release with a 1 in any position") 
	#this also handles a white strip bc it's a 1 either way


def horizontal6wires():
	print("horizontal 6")
	numberOfWires = input("How many wires are there: ")
	wires=[]
	count =1
	if(numberOfWires == 3):
		while(count <= 3):
			wireColor = raw_input("Wire Color: ")
			wires.append(wireColor)
			count = count + 1
		if "red" not in wires:
			print("CUT SECOND")
		elif wires[-1] == wires.index("white"):
			print("CUT LAST WIRE")
		elif wires.count("blue") > 1:
			print("CUST LAST BLUE")
		else:
			print("CUT LAST WIRE")
	if(numberOfWires == 4):
		while(count <= 4):
			wireColor = raw_input("Wire Color: ")
			wires.append(wireColor)
			count = count + 1
		if wires.count("red") > 1:
			oddSerial = raw_input("IS the last digit of the serial Number odd? y/n: ")
			if oddSerial == 'y':
				print("CUT LAST RED")
		elif wires[-1] == wires.index("yellow") and "red" not in wires:
			print("CUT FIRST WIRE")
		elif wires.count("blue") == 1:
			print("CUT FIRST WIRE")
		elif wires.count("yellow") > 1:
			print("CUT LAST WIRE")
		else:
			print("CUST SECOND WIRE")
	if(numberOfWires == 5):
		while(count <= 5):
			wireColor = raw_input("Wire Color: ")
			wires.append(wireColor)
			count = count + 1		
 		if wires[-1] == "black":
 			oddSerial = raw_input("IS the last digit of the serial Number odd? y/n: ")
			if oddSerial == 'y':
				print("CUT FOURTH WIRE")
		elif wires.count("red") == 1 and wires.count("yellow") > 1:
			print("CUT FIRST WIRE")
		elif "black" not in wires:
			print("CUT SECOND WIRE")
		else:
			print("CUT FIRST WIRE")
	if(numberOfWires == 6):
		while(count <= 6):
			wireColor = raw_input("Wire Color: ")
			wires.append(wireColor)
			count = count + 1	
		if "yellow" not in wires:
			oddSerial = raw_input("IS the last digit of the serial Number odd? y/n: ")
			if oddSerial == 'y':
				print("CUT THIRD WIRE")
		elif wires.count("yellow") == 1 and wires.count("white") > 1:
			print("CUT FOURTH WIRE")
		elif "red" not in wires:
			print("CUT LAST WIRE")
		else:
			print("CUT FOURTH WIRE")				
	pass

def abc123wires(): 
	# color = str(input("what color is the wire: ")).lower()
	# letter = str(input("which letter is the wire going to: ")).lower()
	black = ["abc","ac","b","ac","b","bc","ab","c","c"]
	blue = ["b", "ac","b","a","b","bc","c","ac","a"]
	red = ["c","b","a","ac","b","ac","abc","ab","b"]
	blackCount = 0
	blueCount = 0
	redCount = 0
	while 1==1:
		color = str(input("what color is the wire: ")).lower()
		letter = str(input("which letter is the wire going to: ")).lower()
		# print(color)
		# print(letter)
		if color == "black":
			if str(letter) in black[blackCount]:
				print("cut")
			else:
				print("do not cut")
			blackCount += 1

		elif color == "blue":
			if str(letter) in blue[blueCount]:
				print("cut")
			else:
				print("do not cut")
			blueCount += 1

		elif color == "red":
			if str(letter) in red[redCount]:
				print("cut")
			else:
				print("do not cut")
			redCount += 1
		else:
			print("what the fuck is going on ")


def ledStarWires():
	print("ledStarWires") # michael
	pass

def symbolsKeypads():
	print("Symbols")
	count = 1
	list1 = ["oline","at", "lambda", "harryPotter", "octopus", "crazyH","backwardsC" ]
	list2 = ["backwardsEuro","oline", "backwardsC", "co", "star", "crazyH","questionMark" ]
	list3 = ["copyright","ballsack", "co", "ik", "half3", "lambda","star" ]
	list4 = ["fatSix","paragraph", "tb", "octopus", "ik", "questionMark","smile" ]
	list5 = ["trident","smile", "tb", "forwardC", "paragraph", "dragon","star" ]
	list6 = ["fatSix","backwardsEuro", "puzzle", "ae", "trident", "n","omega" ]

	lists = [list1, list2, list3, list4,list5,list6]
	symbols =[]
	order=[]
	while(count <= 4):
		symbols.append(raw_input("Symbol: "))
		count = count + 1
	for list in lists:
		if set(symbols).issubset(list):
			for symbol in symbols:	
				order.append(list.index(symbol))
			order.sort()
			for symbol in order:
				print(list[symbol])	


main()
