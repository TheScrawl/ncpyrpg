import dill as pickle


#Important game function stuff, you probably shouldnt edit this
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

## GAME VARIABLES - Feel free to edit and add things here
playerY, playerX, = 4, 4 #Spawn Point

## GAME MAP ARRAYS AND OBJECTS
# Arrays - These are objects you can draw
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



## USER MAP - put in all of the objects you want to draw and their locations
def drawmap(window):
	drawArray(2, 3, window, house)
	drawArray(button.posY, button.posX, window, button.char)

#You need to put all of the variables you want in the game into this list
varList = ['mapObjList', 'playerY', 'playerX', 'house', 'button']

#Probably dont mess with this either
varDict = dict([i, eval(i)] for i in varList)

#You probably shouldnt touch this either
if __name__ == '__main__':
	pickle.dump(varDict, open('gamefile', 'wb'))
	pickle.dump(drawmapvar, open('functionfile', 'wb'))
