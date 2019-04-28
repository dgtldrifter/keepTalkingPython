
def main():
	print("1: button")
	print("2: 6 horizontal wires")
	print("3: 123abc wires")
	print("4: led star wires")
	print("5: symbols")
	print("6: number keypad")
	print("8: Simon Says)
	puzzle = int(input("which puzzle do you have: "))

	if int(puzzle) == 1: button()
	elif int(puzzle) == 2: horizontal6wires()
	elif int(puzzle) == 3: abc123wires()
	elif int(puzzle) == 4: ledStarWires()
	elif int(puzzle) == 5: symbolsKeypads()
	elif int(puzzle) == 6: numberKeypad()
	elif int(puzzle) == 8: simon()
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
	led = input("LEDs from left to right (y for yes, n for no, include space between each one)?").split()
	star = input("Stars from left to right (y for yes, n for no, include spaces between each one)?").split()
	color = input("Colors of each wire ('red', 'blue', 'rw', 'bw', 'rb', 'white', 'n' for no)").split()
	for i in range(0, 6):
		if color[i] == "n":
			continue
		if led[i] == "y":
			if star[i] == "y":
				if (color[i] == "red" or color[i] == "rw" or color[i] == "white"):
					question = input("Does the bomb have two or more batteries (y/n)?")
					if (question == 'y' or question == "Y"):
						print("Cut")
					else:
						print("Don't Cut")
				elif (color[i] == "blue" or color[i] == "bw"):
					question = input("Does the bomb have a parallel port? (y/n)?")
					if (question == 'y' or question == 'Y'):
						print("Cut")
					else:
						print("Don't Cut")
				elif (color[i] == "rb"):
					print("Don't Cut")
			else:
				if (color[i] == "red" or color[i] == "rw"):
					question = input("Does the bomb have two or more batteries (y/n)?")
					if (question == 'y' or question == "Y"):
						print("Cut")
					else:
						print("Don't Cut")
				elif (color[i] == "blue" or color[i] == "bw"):
					question = input("Does the bomb have a parallel port? (y/n)?")
					if (question == 'y' or question == 'Y'):
						print("Cut")
					else:
						print("Don't Cut")
				elif (color[i] == "rb"):
					question = input("Is the last digit of the serial number even (y/n)?")
					if (question == "y" or question == "Y"):
						print("Cut")
					else:
						print("Don't Cut")
				else:
					print("Don't Cut")
		else:
			if star[i] == "y":
				if (color[i] == "red" or color[i] == "rw" or color[i] == "white"):
					print("Cut")
				elif (color[i] == "blue" or color[i] == "bw"):
					question = input("Is the last digit of the serial number even (y/n)?")
					if (question == "y" or question == "Y"):
						print("Cut")
					else:
						print("Don't Cut")
				elif (color[i] == "rb"):
					question = input("Does the bomb have a parallel port? (y/n)?")
					if (question == 'y' or question == 'Y'):
						print("Cut")
					else:
						print("Don't Cut")
			else:
				if (color[i] == "red" or color[i] == "blue" or color[i] == "rb" or color[i] == "rw" or color[i] == "bw"):
					question = input("Is the last digit of the serial number even (y/n)?")
					if (question == "y" or question == "Y"):
						print("Cut")
					else:
						print("Don't Cut")
				else:
					print("Cut")

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

def numberKeypad():
	print("NumberKeyPad")
	print("Stage 1")
	displayNum = int(input("Display Number: "))
	
	if displayNum == 1:
		print("STAGE1: SECOND POSITION")
		stageLabel1 = int(input("Lable Number: "))
		stagePosition1 = "SECOND POSITION"
		
	elif displayNum == 2:
		print("STAGE1: SECOND POSITION")
		stagePosition1 = "SECOND POSITION"
		stageLabel1 = int(input("Lable Number: "))
		
	elif displayNum == 3:
		print("STAGE1: THIRD POSITION")
		stagePosition1 = "THIRD POSITION"
		stageLabel1 = int(input("Lable Number: "))

	elif displayNum == 4:
		print("STAGE1: FOURTH POSITION")
		stagePosition1 = "FOURTH POSITION"
		stageLabel1 = int(input("Lable Number: "))
		
	else:
		print("FUCK YOU")
		
		
	print("Stage 2")
	displayNum = int(input("Display Number: "))
	if displayNum == 1:		
		print("LABEL 4")
		stageLabel2 = int(input("Lable Number: "))
		stagePosition2 = input("Position of Lable 4: ")
		
	elif displayNum == 2:
		print(stagePosition1)
		stagePosition2 = stagePosition1
		stageLabel2 = int(input("Lable Number: "))
		
	elif displayNum == 3:
		print("FIRST POSITION")
		stagePosition2 = "FIRST POSITION"
		stageLabel2 = int(input("Lable Number: "))

	elif displayNum == 4:
		print(stagePosition1)
		stagePosition2 = stagePosition1
		stageLabel2 = int(input("Lable Number: "))
		
	else:
		print("FUCK YOU")
		
	print("Stage 3")
	displayNum = int(input("Display Number: "))
	if displayNum == 1:		
		
		print("LABEL: "+ str(stageLabel2))
		stagePosition3 = input("Position of Lable: ")
		stageLabel3 = int(input("Lable Number: "))
		
	elif displayNum == 2:		
		print("LABEL: "+ str(stageLabel1))
		stagePosition3 = input("Position of Lable: ")
		stageLabel3 = int(input("Lable Number: "))
		
	elif displayNum == 3:
		print("THIRD POSITION")
		stagePosition3 = "THIRD POSITION"
		stageLabel3 = int(input("Lable Number: "))
		
	elif displayNum == 4:
		print("LABEL 4")
		stagePosition3 = input("Position of Lable 4: ")
		stageLabel3 = int(input("Lable Number: "))
	else:
		print("FUCK YOU")	
		
	print("Stage 4")
	displayNum = int(input("Display Number: "))
	if displayNum == 1:		
		print(stagePosition1)
		stageLabel4 = int(input("Lable Number: "))
		stagePosition4 = stagePosition1
		
	elif displayNum == 2:		
		print("FIRST POSITION")
		stagePosition4 = "FIRST POSITION"
		stageLabel4 = int(input("Lable Number: "))
		
	elif displayNum == 3:
		print(stagePosition2)
		stagePosition4 = stagePosition2
		stageLabel4 = int(input("Lable Number: "))
		
	elif displayNum == 4:
		print(stagePosition2)
		stagePosition4 = stagePosition2
		stageLabel4 = int(input("Lable Number: "))
	else:
		print("FUCK YOU")
		
	print("Stage 5")
	displayNum = int(input("Display Number: "))
	if displayNum == 1:		
		print("LABEL: " + str(stageLabel1))
		
	elif displayNum == 2:		
		print("LABEL: " + str(stageLabel2))
			
	elif displayNum == 3:
		print("LABEL: " + str(stageLabel4))
		
	elif displayNum == 4:
		print("LABEL: " + str(stageLabel3))
		
	else:
		print("FUCK YOU")

		
def simon():
	vowel = input("Is there a vowel on the serial? (y/n)")
	strikes = int(input("What is the number of strikes (0, 1, 2)?"))
		
	colorsVowel = [["Blue", "Red", "Yellow", "Green"], ["Yellow", "Green", "Blue", "Red"], ["Green", "Red", "Yellow", "Blue"]]
	colors = [["Blue", "Yellow", "Green", "Red"], ["Red", "Blue", "Yellow", "Green"], ["Yellow", "Green", "Blue", "Red"]]
		
	if vowel == "y":
		print("Red = ", colorsVowel[strikes][0])
		print("Blue = ", colorsVowel[strikes][1])
		print("Green = ", colorsVowel[strikes][2])
		print("Yellow = ", colorsVowel[strikes][3])
	else:
		print("Red = ", colors[strikes][0])
		print("Blue = ", colors[strikes][1])
		print("Green = ", colors[strikes][2])
		print("Yellow = ", colors[strikes][3])
main()
