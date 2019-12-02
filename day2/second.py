import copy

f = open("input.txt", "r")
realdata = f.read().split(',')
f.close()

realdata = [int(x) for x in realdata]

def process(i, data):
	global output
	opcode = data[i]
	if opcode == 1:
		data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
		process(i+4, data)
	elif opcode == 2:
		data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
		process(i+4, data)
	elif opcode == 99:
		output = data[0]

output = 0
iOne = 0
iTwo = 0
while iOne <= 99:
	while iTwo <= 99:
		loopdata = copy.deepcopy(realdata)
		loopdata[1] = iOne
		loopdata[2] = iTwo
		process(0, loopdata)
		if output == 19690720:
			break
		else:
			iTwo += 1
	if output == 19690720:
		break
	else:
		iOne += 1
		iTwo = 0

print("Found 19690720 using the following inputs: {}, {}".format(iOne, iTwo))
print("Challenge solution is: {}".format((100*iOne)+iTwo))