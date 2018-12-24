pos = [0]*10, [0]*10
x, y = 1, 1

def drawmap(x, y):
	for i in range(10):
		for j in range(10):
			if i == y and j == x:
				print ("x", end = " ")
			else:
				print ("0", end = " ")
		print("")

drawmap(x, y)
while True:
	movement = input("Please enter W, S, A, or D")
	if movement.upper() == 'A':
		x -= 1
	elif movement.upper() == 'S':
		y += 1
	elif movement.upper() == 'D':
		x += 1
	elif movement.upper() == 'W':
		y -= 1
	#elif movement.upper() == 'EXIT':
		#close game

	drawmap(x, y)

#limit movement to map, figure out how to make exit command work,
#dont redraw map every time
