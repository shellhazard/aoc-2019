f = open("input.txt", "r")
data = f.read().split(',')
f.close()

data =  [int(x) for x in data]
data[1] = 12
data[2] = 2

print(data)
def process(i):
	opcode = data[i]
	if opcode == 1:
		data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
		process(i+4)
	elif opcode == 2:
		data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
		process(i+4)
	elif opcode == 99:
		return

i = 0
process(i)
print(data)