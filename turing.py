#In "The Emperor's New Mind" Sir Roger Penrose describes a kind of universal Turing Machine which accepts as its input descriptions of other turing machines, enocded in binary - this program seeks to emulate such a machine
#Mahmoud Ghanem - Summer 2014

def convertMotion(motion):
	##0 = R, 1 = L, 2 = STOP
	if motion == "R": motion = 0
	elif motion == "L": motion = 1
	elif motion == "S": motion = 2
	return motion

def convertOperation(output, motion):
	return int(motion)*2 + int(output)

def loadLogicFromDecimal(tapeString):
	pass

def loadLogicFromBinary(tapeString):
	"""
	Penrose describes a kind of binary notation which sandwiches unary numbers inbetween 0s
	He then interperets unary numbers other than 1s and 0s as punctuation using the following rules

	2 = L
	3 = R
	4 = S

	To economise on space, he drops 0s off both ends of the binary input string and in the middle of it, where zeros would otherwise be expected...
	"""
	pass

def loadLogicFromPenrose(tapeString):
	"""
	FORMAT for "Penrose Style" turing descriptions (see page 54 of the emperor's new mind Vintage 1990)
	for example UN+1 can be encoded as "00->00R,01->11R,10->01S,11->11R"
	"""
	program = {}
	instructions = tapeString.split(",")
	for instruction in instructions:
		state = int(instruction.split("->")[0][0:-1])
		condition = int(instruction.split("->")[0][-1])
		newstate = int(instruction.split("->")[1][0:-2])
		output = int(instruction.split("->")[1][-2])
		motion = convertMotion(instruction.split("->")[1][-1])
		if not state in program:
			program[state] = {}
		program[state][condition] = (convertOperation(output, motion), newstate)
	print(program)
	return program


def loadLogicFromFile(file, type = "bin"):
	pass


if __name__ == "__main__":
	tape = [1,1,1,1,0,0,0,0]
	state = 0
	position = 0
	"""
	FORMAT for state table:
	logic_table[0][0] -> what to do on encountering a  0 in state 0
	logic_table[5][1] ->what to do on encountering a 1 in state 5

	so if logic_table[6][0] = (1,7) perform operation 1, then go to state 7 on encouterning a 0 when in state 6

	KEY for operations:
	0:write 0 move right
	1:write 1 move right
	2:write 0 move left
	3:write 1 move left
	4:write 0 HALT
	5:write 1 HALT
	"""
	unaryPlusOne = [
					[ (0, 0), (1, 1) ],
					[ (5, 1), (1, 1) ]
				  ]
	copy = [
				[(4, 0), (0, 1)],
				[(0, 2), (1, 1)], 
				[(3, 3), (1, 2)],
				[(2, 4), (3, 3)],
				[(1, 0), (3, 4)]
			]
	unaryEuclid = loadLogicFromPenrose("00->00R,01->11R,10->01S,11->11R") #NOTE: this only implements unaryPlusOne for the time being
	logic_table=unaryEuclid
	print(tape)
	while 1:
		#extend tape if required
		if position == len(tape):
			tape.append(0)

		if position == -1 :
			tape.insert(0,0)
			position = 0

		current_symbol = tape[position]
		current_instruction, next_state = logic_table[state][current_symbol]

		if current_instruction == 5:
			tape[position] = 1
			break
		elif current_instruction == 4:
			tape[position] = 0
			break
		elif current_instruction == 3:
			tape[position] = 1
			position -= 1
		elif current_instruction == 2:
			tape[position] = 0
			position -= 1
		elif current_instruction == 1:
			tape[position] = 1
			position += 1
		elif current_instruction == 0:
			tape[position] = 0
			position += 1
		state = next_state
	print(tape)
