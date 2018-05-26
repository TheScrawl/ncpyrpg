# Engine functions and variables - do not touch
mapObjList = []

def drawArray(y, x, window, array): 
	for i in array: 
		window.addstr(y, x, i) 
		y = y + 1 

class mapObj(object):
	global mapObjList
	def __init__(self, char, posY, posX, function):
		self.char = char
		self.posY = posY
		self.posX = posX
		self.pos = (self.posY, self.posX)
		self.function = function
		mapObjList.append(self)	
# Game Variables

playerY, playerX, = 4, 4 #Spawn Point

# Game Map Arrays and Objects


house = [
	'##########',
	'#        #',
	'#        #',
	'#        #',
	'#        #',
	'##########',
	' ',
	'hint: x is a button'
	]

# User map
def drawmap(window):
	drawArray(2, 3, window, house)
	button = mapObj(['x'], 6, 6, 'window.addch(7, 6, " ")')
	drawArray(button.posY, button.posX, window, button.char)
