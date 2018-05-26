## ENGINE FUNCTIONS AND VARIABLES - do not touch
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
## GAME VARIABLES
playerY, playerX, = 4, 4 #Spawn Point

## GAME MAP ARRAYS AND OBJECTS
# Arrays
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
# Objects (char, y, x, function)
button = mapObj(['x'], 6, 6, 'window.addch(7, 6, " ")')

## USER MAP
def drawmap(window):
	drawArray(2, 3, window, house)
	drawArray(button.posY, button.posX, window, button.char)
