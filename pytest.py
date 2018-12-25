import os
x, y = 1, 1
def drawmap(x, y):
	for i in range(10):
		for j in range(10):
			if i == y and j == x:
				print ("x", end = " ")
			else:
				print ("0", end = " ")
		print("")

while True:
	os.system("cls")
	drawmap(x, y)
	movement = input("""Please enter W, S, A, or D
""")
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
	if x>9:
		x = 9
	elif y>9:
		y = 9
	elif y<0:
		y = 0
	elif x<0:
		x = 0


#figure out how to make exit command work, tidy up code, mery crimis
